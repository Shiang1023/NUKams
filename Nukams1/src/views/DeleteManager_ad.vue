<template>
  <div class="wrapper">
    <nav>
      <aside>
        <router-link to="DeleteManager_ad">廣告</router-link>
        <router-link to="DeleteManager_post">貼文</router-link>
        <router-link to="DeleteManager_comment">留言</router-link>
      </aside>
    </nav>
    <main>
      <div v-for="advertisement in advertisements" :key="advertisement.ad_id" class="button-container">
        <div class="button">
          {{ advertisement.ad_id }} {{ advertisement.title }}
          <div class="delete-button" @click="confirmDelete(advertisement.ad_id)">刪除</div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'DeleteManager_advertisement',
  data() {
    return {
      advertisements: [],
    };
  },
  created() {
    this.getAdvertisements();
  },
  methods: {
    getAdvertisements() {
      const path = 'http://127.0.0.1:5000/api/get_all_advertisement';
      axios.get(path)
        .then((res) => {
          this.advertisements = res.data.ad_info;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    deleteAdvertisement(adId) {
      const deletePath = `http://127.0.0.1:5000/api/delete_advertisement/${adId}`;
      axios.get(deletePath)
        .then((res) => {
          console.log('Advertisement deleted successfully:', res.data);
          this.getAdvertisements(); // Refresh advertisements after deletion
        })
        .catch((error) => {
          console.error('Error deleting advertisement:', error);
        });
    },
    confirmDelete(adId) {
      if (window.confirm('確定要刪除這則廣告嗎？')) {
        this.deleteAdvertisement(adId);
      } else {
        // User clicked cancel, do nothing
      }
    },
  },
};
</script>

<style scoped>
.wrapper {
  display: flex;
}

nav {
  position: fixed;
  top: 50%; /* 垂直居中 */
  left: 0;
  transform: translateY(-50%); /* 将元素上移自身高度的一半以实现居中 */
  padding-left: 200px;
}

aside {
  background-color: #f1f1f1;
  width: 100px; /* 调整宽度 */
  padding: 10px;
  box-shadow: 2px 0 5px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  align-items: center; /* 水平居中 */
}

aside a {
  display: block;
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  background-color: #2d68a894;
  color: white;
  font-size: 16px;
  text-align: center;
  text-decoration: none;
}

aside a:hover {
  background-color: #1a4e7a;
}

main {
  margin-left: 120px; /* 为主内容区域留出更多空间 */
  flex-grow: 1;
}

.button-container {
  text-align: center; /* 按钮置中 */
  position: relative; /* 相对定位 */
  margin-bottom: 10px; /* 增加按钮间距 */
}

.button {
  position: relative; /* 相对定位 */
  width: 600px; /* 设置按钮宽度 */
  background-color: #2d68a894; /* 初始按钮颜色 */
  color: #fff; /* 文字颜色 */
  border: none; /* 移除按钮边框 */
  border-radius: 5px; /* 圆角按钮 */
  padding: 10px 20px; /* 调整内部填充 */
  cursor: pointer; /* 鼠标悬停时显示手指指针 */
  transition: background-color 0.3s; /* 添加颜色过渡效果 */
  text-align: left; /* 文字靠左对齐 */
}

.confirm-button,
.delete-button {
  position: absolute; /* 绝对定位 */
  top: 0; /* 与父元素顶部对齐 */
  width: 50px; /* 设置按钮宽度 */
  background-color: green; /* 确认按钮背景色 */
  color: #fff; /* 文字颜色 */
  border: none; /* 移除按钮边框 */
  border-radius: 5px; /* 圆角按钮 */
  padding: 5px; /* 内部填充 */
  cursor: pointer; /* 鼠标悬停时显示手指指针 */
  transition: background-color 0.3s; /* 添加颜色过渡效果 */
}

.delete-button {
  right: 0; /* 与父元素右边对齐 */
  background-color: red; /* 删除按钮背景色 */
}

.confirm-button {
  right: 55px; /* 与父元素右边保持一定的间距 */
}

.confirm-button:hover,
.delete-button:hover {
  background-color: darkgreen; /* 鼠标悬停时的按钮颜色 */
}
</style>
