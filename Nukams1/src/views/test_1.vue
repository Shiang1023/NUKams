<template>
  <div id="app">
    <header>
      <h1>管理員系統</h1>
    </header>
    
    <nav>
      <router-link to="/ADSmain/ADS">首頁</router-link>
      <router-link :to="{name:'VertifyManager_ad'}">審核</router-link>
      <router-link :to="{name:'DeleteManager_ad'}">刪除</router-link>
      <router-link :to="{name:'AccountManager_student'}">帳號管理</router-link>
      <router-link to='#'>管理員帳號</router-link>
      <!-- <router-link :to="{name:'editRecordSelectName'}">編輯訪視紀錄</router-link> -->
       <!-- <router-link :to="{name: 'personalINFO_tea', params: { id: 'T110112' }}">個人基本資料</router-link> -->
    </nav>
    
    <div class="content">
      
      
      <main>
        <router-view> </router-view>
        <!-- <h2>歡迎來到管理員系統!</h2> -->
      </main>
    </div>
    <footer>
      &copy; 2023 校外租屋系統. All rights reserved.
    </footer>
  </div>
  
</template>

<script>
export default {
  name: 'RentingSystem',
  methods: {
    navigateTo(route) {
      this.$router.push(route);
    }
  }
}
</script>

<style scoped>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f5f5f5;
  color: #333;
  height: 100vh;
  display: flex;
  flex-direction: column;
}
header {
  background-color: #2d68a894;
  color: #fff;
  padding: 20px;
  text-align: center;
}
nav {
  background-color: #f1f1f1;
  padding: 10px;
  text-align: center;
}
nav a {
  color: #333;
  text-decoration: none;
  padding: 10px;
  margin: 5px;
}
nav a:hover {
  background-color: #ddd;
}
.content {
  display: flex;
  flex: 1;
  overflow: hidden;
}
aside {
  background-color: #f1f1f1;
  width: 200px;
  padding: 10px;
  box-shadow: 2px 0 5px rgba(0,0,0,0.1);
}
aside button {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  background-color: #2d68a894;
  color: white;
  font-size: 16px;
}
aside button:hover {
  background-color: #1a4e7a;
}
main {
  padding: 20px;
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%; 
  overflow: auto; 
}
footer {
  background-color: #2d68a894;
  color: #fff;
  padding: 10px;
  text-align: center;
  position: relative;
  width: 100%;
}
</style>