<template>
  <div class="wrapper">
    <nav>
      <aside>
        <router-link to="AccountManager_student">學生</router-link>
        <router-link to="AccountManager_teacher">老師</router-link>
        <router-link to="AccountManager_landlord">房東</router-link>
      </aside>
    </nav>
    <main>
      <div v-for="landlord in landlords" :key="landlord.id" class="button-container">
        <router-link :to="{ name: 'personalINFO_landlord', params: { id: landlord.id } }" class="button">
          <div class="landlord-info">
            <span>{{ landlord.id }} {{ landlord.name }}</span>
          </div>
        </router-link>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AccountManager_landlord',
  data() {
    return {
      landlords: [], // Array to hold landlord data
    };
  },
  created() {
    this.getLandlords();
  },
  methods: {
    getLandlords() {
      const path = 'http://127.0.0.1:5000/api/administrator/get_idandnames/1';
      console.log(path);
      axios.get(path)
        .then((res) => {
          this.landlords = res.data.all_idandnames_info; // Update to use correct data structure
          console.log(this.landlords);
        })
        .catch((error) => {
          console.error(error);
        });
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
  display: flex;
  align-items: center;
  justify-content: center;
  width: 600px; /* 设置按钮宽度 */
  background-color: #2d68a894; /* 初始按钮颜色 */
  color: #fff; /* 文字颜色 */
  border: none; /* 移除按钮边框 */
  border-radius: 5px; /* 圆角按钮 */
  padding: 10px 20px; /* 调整内部填充 */
  cursor: pointer; /* 鼠标悬停时显示手指指针 */
  transition: background-color 0.3s; /* 添加颜色过渡效果 */
  text-align: center; /* 文字居中对齐 */
}

.button:hover {
  background-color: #1e4b7e; /* 鼠标悬停时的按钮颜色 */
}

.landlord-info {
  display: flex;
  justify-content: center;
  width: 100%;
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
