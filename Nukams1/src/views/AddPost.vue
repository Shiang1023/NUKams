<template>
  <div class="menu">
    <button @click="$router.back()">Back</button>
  </div>
  <div class="main">
    <div class="post-card">
      <div class="post-header">
        <img :src="publicPath + post.avatar" alt="Avatar" class="avatar" />
        <div class="username">{{ post.username }}</div>
      </div>
      <div class="post-image">
        <input 
          ref="inputDOM"
          type="file"
          class="upload"
          name="imgUpload"
          multiple="multiple"
          @change="fileChange"
        />
        <button @click="uploadImages" class="UPD">上傳照片</button>
        <div v-if="Object.keys(previewMap).length !== 0" class="img_box">
          <div v-for="(item, idx) in previewMap" :key="idx" class="img-item">
            <img :src="item" alt="" />
          </div>
        </div>
      </div>
      <div class="post-content">
        <input type="text" v-model="msg" placeholder="輸入貼文內容..." id="content" />
      </div>
      <button @click="upload" class="UPD">Upload</button>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

const publicPath = '/pic/';

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

  const setFile = async (fileArr = []) => {
    initData();
    previewMap.value = useQueuePreview(fileArr);
    files.value = fileArr;
    console.log(previewMap.value);
  };

  return { setFile, previewMap, files };
}

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    const isUserPost = computed(() => route.params.username === 'your-username'); // Adjust accordingly
    const { setFile, previewMap, files } = useFileUpdate();
    const inputDOM = ref(null);

    const msg = ref('');
    const post = ref({
      username: '醉了',
      avatar: '',
      content: '',
      id: '',
      image: '',

    });

    const fileChange = (e) => {
      console.log(e.target.files);
      setFile(e.target.files);
    };

    const uploadImages = () => {
      inputDOM.value.click();
    };

    const upload = async () => {
      post.value.content = msg.value;
      
      const formData = new FormData();
      formData.append('username', post.value.username);
      formData.append('content', post.value.content);
      
      // Append all files to FormData
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
        post.value.image = imageUrls;
        post.value.id = route.params.username;

      } catch (error) {
        console.error(error);
      }

      const path = `http://127.0.0.1:5000/api/insert_post/${post.value.id},${post.value.content},${post.value.image}`;
      console.log(path);
      axios.get(path)
        .then((res) => {
          console.log("succeed");
          router.push('/post');  // 跳转到貼文列表页面
        })
        .catch((error) => {
          console.error(error);
        });
    };

    return {
      publicPath,
      post,
      msg,
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
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  width: 100vw;
}
.post-card {
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  border-radius: 8px;
  /* 陰影 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.537);
  overflow: hidden;
  margin-bottom: 10px;
  width: 60%;
  max-width: 1000px;
  background-color: rgb(215, 219, 225);
  color: rgb(0, 0, 0);
}

.post-header {
  display: flex;
  align-items: center;
  padding: 10px;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}

.username {
  font-weight: bold;
}

.post-image {
  position: relative;
  width: 100%;
  height: 300px; /* 固定高度 */
  overflow: hidden;
  background-color: #eee;
}

.img_box {
  display: flex;
  flex-wrap: wrap;
  overflow-y: auto;
  height: 100%;
  height: 300px; /* 設置圖片框的高度 */
}

.img-item {
  flex: 1 1 auto;
  margin: 5px;
  min-width: 100px; /* 最小寬度 */
  max-width: 150px; /* 最大寬度 */
  max-height: 100px; /* 最大高度 */
}

.img-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.post-content {
  padding: 10px;
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
  margin: 10px;
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
