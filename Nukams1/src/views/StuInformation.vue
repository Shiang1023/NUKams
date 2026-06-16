<template>
  <div id="app">
    <main>
      <div class="user-info">
        <h2>學生基本資料</h2>
        <div v-if="!isEditing">
          <p><span>姓名:</span> {{ user.name }}</p>
          <p><span>學號:</span> {{ user.student_id }}</p>
          <p><span>年級:</span> {{ user.grade }}</p>
          <p><span>導師:</span> {{ tea.tea_name }}</p>
          <p><span>性別:</span> {{ displayGender }}</p>
          <p><span>電子郵件:</span> {{ user.email }}</p>
          <p><span>電話號碼:</span> {{ user.phone }}</p>
          <p><span>家裡地址:</span> {{ user.home_address }}</p>
          <p><span>家裡電話:</span> {{ user.home_phone }}</p>
          <p><span>家裡聯絡人:</span> {{ user.home_contact }}</p>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import Tcs_nav from '@/components/Tcs_nav.vue';
import axios from 'axios';
</script>

<script>
import { createApp, ref } from 'vue';

export default {
  name: 'StuInformation',
  data() {
    return {
      isEditing: false,
      user: {},
      tea: {},
    };
  },
  created() {
    this.getStuInfo(this.$route.params.id);
  },
  computed: {
    displayGender() {
      return this.user.gender === 1 ? '男' : '女';
    },
  },
  methods: {
    toggleEdit() {
      this.isEditing = !this.isEditing;
    },
    getStuInfo(id) {
      const path = `http://localhost:5000/stu_info/${id}`;
      axios
        .get(path)
        .then((res) => {
          this.user = res.data.stu_info;
          this.getTeaName(this.user.teacher_id); // 调用getTeaName方法
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getTeaName(tid) {
      const path = `http://localhost:5000/tcs_TeaName/${tid}`;
      axios
        .get(path)
        .then((res) => {
          if (Array.isArray(res.data.names) && res.data.names.length > 0) {
            this.tea = res.data.names[0];
          } else {
            // 处理没有找到教师姓名的情况
            this.tea = { tea_name: '未知' };
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>
 body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      min-height: 100vh;
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
      padding: 20px;
      flex: 1;
    }
    main button {
      font-size: 1.2em;
      margin: 10px;
    }
    .user-info {
      max-width: 600px;
      margin: 0 auto;
      background-color: #f9f9f9;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      text-align: left;
    }
    .user-info h2 {
      text-align: center;
      color: #333;
    }
    .user-info p, .user-info input {
      font-size: 18px;
      line-height: 1.6;
      color: #555;
      margin: 10px 0;
    }
    .user-info p span {
      font-weight: bold;
      color: #333;
    }
    .user-info input {
      width: 100%;
      padding: 10px;
      margin-bottom: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    .user-info button {
      padding: 10px 20px;
      background-color: #2d68a894;
      color: #fff;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      margin: 10px 5px;
    }
    .user-info button:hover {
      background-color: #1a4e7a;
    }
    footer {
      background-color: #2d68a894;
      color: #fff;
      padding: 10px;
      text-align: center;
      position: relative;
      width: 100%;
      bottom: 0;
    } body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      min-height: 100vh;
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
      padding: 20px;
      flex: 1;
    }
    main button {
      font-size: 1.2em;
      margin: 10px;
    }
    .user-info {
      max-width: 600px;
      margin: 0 auto;
      background-color: #f9f9f9;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .user-info h2 {
      text-align: center;
      color: #333;
    }
    .user-info p, .user-info input {
      font-size: 18px;
      line-height: 1.6;
      color: #555;
      margin: 10px 0;
    }
    .user-info p span {
      font-weight: bold;
      color: #333;
    }
    .user-info input {
      width: 100%;
      padding: 10px;
      margin-bottom: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    .user-info button {
      padding: 10px 20px;
      background-color: #2d68a894;
      color: #fff;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      margin: 10px 5px;
    }
    .user-info button:hover {
      background-color: #1a4e7a;
    }
    footer {
      background-color: #2d68a894;
      color: #fff;
      padding: 10px;
      text-align: center;
      position: relative;
      width: 100%;
      bottom: 0;
    }
</style>
