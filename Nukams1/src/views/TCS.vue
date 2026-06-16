<template>
  <div class="main">
    <div class="Up_Nav">
      <Up />
      <nav>
        <router-link :to="{name:'TCS'}">首頁</router-link>
        
        <router-link :to="{ name: 'editRecordSelectName', params: { id: username } }">訪視紀錄</router-link>
          
        <div class="dropdown">
          <router-link :to="{name:'stuManage'}">學生管理▼</router-link>
          <div class="dropdown-content">
            <router-link :to="{name:'StuPersonalSelectName', params: { id: username }}">學生基本資料</router-link>
            <router-link :to="{name:'StuAccSelectName',params: { id: username }}">學生住宿資料</router-link>
            <router-link :to="{name:'StuRecordSelectName',params: { id: username }}">學生訪視紀錄</router-link>
          </div>
        </div>
        <router-link :to="{name: 'personalINFO_tea', params: { id: username }}">個人基本資料</router-link>
      </nav>
    </div>
    <main>
      <RouterView></RouterView>
    </main>
    
    <Down />
  </div>
</template>
  
<script setup>
    import Up from '../components/Up.vue'
    import Down from '../components/Down.vue'
    import Tcs_nav from '@/components/Tcs_nav.vue';
    import router from '@/router';
    import { useRoute } from 'vue-router';

    const route = useRoute();
    const username = route.params.username;
 
</script>
  
<style scoped>
  .Up_Nav{
    display: flex;
    justify-content:flex-start;
    flex-direction: column;
    color: #fff;
    width: 100%;
  }
  .main{
    height: 100%;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content:space-between; 
    width: 100%;
  }
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: block;
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
  .dropdown {
    position: relative;
    display: inline-block;
  }
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f1f1f1;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    z-index: 1;
  }
  .dropdown-content a {
    color: #333;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
  }
  .dropdown-content a:hover {
    background-color: #ddd;
  }
  .dropdown:hover .dropdown-content {
    display: block;
  }
  main {
    padding: 20px;
  }
  
  </style>
  