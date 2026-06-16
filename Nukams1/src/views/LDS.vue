<template>
  <div id="app">
    <header>
      <h1>房東管理系統</h1>
    </header>
    
    <nav>
      <router-link :to="{name:'LDS'}">首頁</router-link>
      <router-link :to="{name:'LeaseAndRenter', params: { id: username }}">租戶與租約管理</router-link>
      <router-link :to="{name:'MaintanceNotice', params: { id: username }}">維修通知管理</router-link>
      <router-link :to="{name:'personalINFO_LDS', params: { id: username }}">個人基本資料</router-link>
      <!-- <router-link :to="{name:'editRecordSelectName'}">編輯訪視紀錄</router-link> -->
       <!-- <router-link :to="{name: 'personalINFO_tea', params: { id: 'T110112' }}">個人基本資料</router-link> -->
    </nav>
    
    <div class="content">
      
      
      <main>
        <router-view> </router-view>
        <!-- <h2>歡迎來到房東管理系統!</h2>
        <p>這裡是房東可用的管理功能網頁</p>
        <h3>功能特色:</h3>
        <ul>
          <li>租戶與租約管理: 可以新增、修改、刪除、查詢租約與租戶。</li>
          <li>維修通知管理: 可以新增、修改、刪除、查詢修繕計畫與查看和刪除，修繕通知。</li>
          <li>個人基本資料: 可以修改個人基本資訊。</li>
        </ul> -->
      </main>
    </div>
    <footer>
      &copy; 2023 校外租屋系統. All rights reserved.
    </footer>
  </div>
  
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();
const username = route.params.username;


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
  padding: 10px;
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