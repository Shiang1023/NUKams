<template>
  <nav>
    <router-link to="/STS">首頁</router-link>
    <router-link to="/personalInfo_st">個人資料</router-link>
    <router-link to="#">廣告</router-link>
    <router-link to="#">留言</router-link>
    <router-link to="#">貼文</router-link>
    <div class="dropdown">
      <router-link to="#">學生功能選單</router-link>
      <div class="dropdown-content">
        <router-link to="/Accommodation_st">校外住宿資料</router-link>
        <router-link to="/FillinRecord_st">訪視表單</router-link>
        <router-link to="/Repair_st">修繕表單</router-link>
        <router-link to="/VisitTime_st">訪視日期填寫</router-link>
      </div>
    </div>
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
</style>
