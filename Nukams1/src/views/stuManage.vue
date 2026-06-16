<template>
  <div id="app">
    <div class="SM_main">
      <button class="SVRM" @click="goToTestPage('StuPersonalSelectName', 'T10912')">學生基本資料</button>
      <button class="SVRM" @click="goToTestPage('StuAccSelectName', 'T10912')">學生住宿資料</button>
      <button class="SVRM" @click="goToTestPage('StuRecordSelectName', 'T10912')">學生訪視紀錄</button>
    </div>
  </div>
</template>

<script setup>
import Tcs_nav from '@/components/Tcs_nav.vue';
import { useRouter } from 'vue-router';
const router = useRouter();

const goToTestPage = (page, id) => {
  router.push({ name: page, params: { id } });
};
</script>


<style scoped>
  .SM_main {
    display: flex;

  
  justify-content: center;
  align-items: center;
  padding: 20px;
  text-align: center;
  }
  /* CSS styles go here */
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
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
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
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
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: row;
    padding: 20px;
    text-align: center;
  }
 
  footer {
    background-color: #2d68a894;
    color: #fff;
    padding: 10px;
    text-align: center;
    position: absolute;
    bottom: 0;
    width: 100%;
  }
  .SVRM {
  display: inline-block;
  font-size: 1.2em;
  margin: 10px;
  padding: 10px 20px;
  color: #000;
  background-color: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 150px;
}

.SVRM:hover {
  background-color: #8d8a8a; /* Slightly darker background on hover */
}

</style>