<template>
  <div class="menu">
    <button @click="$router.back()">Back</button>
  </div>
  <div class="main">
    <div class="ad-card">
      <div class="ad-image">
        <input 
          ref="inputDOM"
          type="file"
          class="upload"
          name="imgUpload"
          multiple
          @change="fileChange"
        />
        <button @click="uploadImages" class="UPD">上傳照片</button>
        <div v-if="Object.keys(previewMap).length !== 0" class="img_box">
          <div v-for="(item, idx) in previewMap" :key="idx" class="img-item">
            <img :src="item" alt="" />
          </div>
        </div>
      </div>
      <div class="ad-content">
        <input type="text" v-model="ad.title" placeholder="輸入廣告標題..." />
        <input type="text" v-model="ad.price" placeholder="輸入價格..." />
        <input type="text" v-model="ad.address" placeholder="輸入地址..." />
        <input type="text" v-model="ad.description" placeholder="輸入廣告內容..." />
        <input type="text" v-model="ad.buildtype" placeholder="輸入建築種類..." />
        <input type="text" v-model="ad.buildyear" placeholder="輸入建築年分..." />
      </div>
      <button @click="upload" class="UPD">Upload</button>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

function useImageFilePreview(file) {
  return window.URL.createObjectURL(file);
}

function useQueuePreview(fileArr) {
  const previewMap = {};
  let idx = 0;
  for (const file of fileArr) {
    const fileData = useImageFilePreview(file);
    previewMap[idx] = fileData;
    idx++;
  }
  return previewMap;
}

export function useFileUpdate() {
  const previewMap = ref({});
  const files = ref([]);

  const initData = () => {
    previewMap.value = {};
    files.value = [];
  };

  const setFile = (fileArr = []) => {
    initData();
    previewMap.value = useQueuePreview(fileArr);
    files.value = fileArr;
  };

  return { setFile, previewMap, files };
}

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    const isUserPost = computed(() => route.params.username === 'your-username'); // 根据实际情况调整
    const { setFile, previewMap, files } = useFileUpdate();
    const inputDOM = ref(null);

    const ad = ref({
      id: '',
      title: '',
      description: '',
      image: '',
      price: '',
      address: '',
      buildtype: '',
      buildyear: '',
    });

    const fileChange = (e) => {
      setFile(e.target.files);
    };

    const uploadImages = () => {
      inputDOM.value.click();
    };

    const upload = async () => {
      const formData = new FormData();
      formData.append('username', route.params.username);
      formData.append('title', ad.value.title);
      formData.append('price', ad.value.price);
      formData.append('address', ad.value.address);
      formData.append('description', ad.value.description);

      for (let i = 0; i < files.value.length; i++) {
        formData.append('images', files.value[i]);
      }

      try {
        const response = await axios.post('http://localhost:3000/posts', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        const imageUrls = response.data.image;
        ad.value.image = imageUrls;
        ad.value.id = route.params.username;

      } catch (error) {
        console.error(error);
      }

      const path = `http://127.0.0.1:5000/api/advertisement/insert_advertisement/${ad.value.id},${ad.value.title},${ad.value.price},${ad.value.address},${ad.value.description},${ad.value.buildtype},${ad.value.buildyear},${ad.value.image}`;
      
      axios.get(path)
        .then((res) => {
          console.log(path);
          router.push(`/advertisement/${route.params.username}`);
        })
        .catch((error) => {
          console.error(error);
        });
    };

    return {
      ad,
      previewMap,
      inputDOM,
      fileChange,
      uploadImages,
      upload,
    };
  },
};
</script>

<style scoped>
.main {
  height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100vw;
  background-color: rgb(213, 222, 226);
}

.ad-card {
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.537);
  overflow: hidden;
  width: 60%;
  max-width: 1000px;
  background-color: rgb(215, 219, 225);
  color: rgb(0, 0, 0);
  height: auto;
  margin-bottom: 20px;
}

.ad-image {
  position: relative;
  width: 100%;
  height: auto;
  background-color: #eee;
  padding: 20px;
}

.img_box {
  display: flex;
  flex-wrap: wrap;
  overflow-y: auto;
  max-height: 300px;
}

.img-item {
  flex: 1 1 auto;
  margin: 5px;
  min-width: 100px;
  max-width: 150px;
  max-height: 100px;
}

.img-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.ad-content {
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

.ad-content input {
  width: 100%;
  height: 40px;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.upload {
  display: none;
}

.UPD {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  margin: 10px 0;
}

.UPD:hover {
  background-color: #0056b3;
}

#content {
  width: 100%;
}

.menu {
  width: 10%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  padding: 20px;
  color: black;
  margin: 10px;
}

.menu button {
  background-color: rgb(22, 55, 69);
  color: rgb(255, 255, 255);
  font-size: large;
  font-weight: bold;
  font-family: 'Times New Roman', Times, serif;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  width: 100%;
  max-height: 56.8px;
  min-width: 70px;
}

.menu button:hover {
  background-color: rgb(23, 46, 56);
  color: rgb(213, 222, 226);
}
</style>
