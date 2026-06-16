<template>
  <nav>
    <router-link to="/TCS">首頁</router-link>
    <div class="dropdown">
      <router-link to="/visitRecordManager">訪視紀錄▼</router-link>
      <div class="dropdown-content">
        <router-link to="/fillRecordSelectName">填寫訪視紀錄</router-link>
        <router-link to="/editRecordSelectName">編輯訪視紀錄</router-link>
      </div>
    </div>
    <div class="dropdown">
      <router-link to="/stuManage">學生管理▼</router-link>
      <div class="dropdown-content">
        <router-link to="/StuPersonalSelectName">學生基本資料</router-link>
        <router-link to="/StuAccSelectName">學生住宿資料</router-link>
        <router-link to="/StuRecordSelectName">學生訪視紀錄</router-link>
      </div>
    </div>
    <router-link to="/personalINFO_tea">個人基本資料</router-link>
  </nav>
</template>

<style scoped>
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
</style>
