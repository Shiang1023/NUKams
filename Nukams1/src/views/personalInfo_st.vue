<template>
  <div id="app">
  <!-- <header>
      <h1>個人基本資料</h1>
  </header>
  <StudentFunction /> -->
  <div class="user-info">
    <h2>個人資料</h2>
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
      <button type="button" @click="toggleEdit">修改</button>
    </div>
    <form v-else @submit.prevent="updateUserInfo">
      
      <label>姓名</label>
      <input type="text" v-model="user.name">
      <br>
      <label>學號</label>
      <input type="text" v-model="user.student_id" disabled>
      <br>
      <label>年級</label>
      <input type="text" v-model="user.grade">
      <br>
      <label>導師</label>
      <input type="text" v-model="tea.tea_name">
      <br>
      <label>性別</label>
      <input type="text" v-model="displayGender">
      <br>
      <label>電子郵件</label>
      <input type="text" v-model="user.email">
      <br>
      <label>電話號碼</label>
      <input type="text" v-model="user.phone">
      <br>
      <label>家裡地址</label>
      <input type="text" v-model="user.home_address">
      <br>
      <label>家裡電話</label>
      <input type="text" v-model="user.home_phone">
      <br>
      <label>家裡聯絡人</label>
      <input type="text" v-model="user.home_contact">
      <br>
      
      <button type="submit">完成</button>
    </form>
  </div>
  <!-- <footer class="Pfooter">
      &copy; 2023 校外租屋系統. All rights reserved.
  </footer> -->

</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'personalINFO_st',
  data() {
    return {
      user: {
        // name: '',
        // student_id: '',
        // grade: '',
        // teacher_id: '',
        // gender: '',
        // email: '',
        // phone: '',
        // home_address: '',
        // home_phone: '',
        // home_contact: ''
      },
      tea: {
      },
      isEditing: false,
    };
  },
  created() {
    this.getUserInfo(this.$route.params.st_id);
  },
  computed:{
    displayGender() {
      return this.user.gender === 1 ? '男' : '女';
    }
  },
  methods: {
    getUserInfo(id) {
      const path = `http://localhost:5000/info/${id}`;
      axios.get(path)
        .then((res) => {
          if (res.data.info) {
            this.user = res.data.info;
            this.getTeaName(this.user.teacher_id);
          } else {
            console.error('User info not found');
          }
        })
        .catch((error) => {
          console.error(error);
        });

    },
    updateUserInfo() {
      const path = `http://localhost:5000/info/${this.user.id}`;
      console.log("Updating user info with data: ", this.user);
      axios.post(path, this.user)
        .then(response => {
          console.log('Update successful', response);
          this.getUserInfo(this.user.id); // 重新獲取用戶資訊
          this.toggleEdit(); // 切換回非編輯模式
        })
        .catch(error => {
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
    toggleEdit() {
      this.isEditing = !this.isEditing;
    }
  }
};
</script>


<style scoped>
.user-info {
  /* max-width: 600px; */
  /* margin: 0 auto; */
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: left;
  margin-left:300px;
  margin-right:150px;
  margin-top: 30px;
  margin-bottom: 10px;
  height: 100%;
  width: 50%;
  max-height: 530px; /* 限制最大高度 */
  overflow-y: auto; /* 添加垂直滚动条 */
}

.user-info h2 {
  text-align: center;
  color: #333;
}

.user-info p,
.user-info input {
  font-size: 18px;
  line-height: 1.6;
  color: #555;
  margin: 10px 0;
  margin-left: 30px;
  
}

.user-info p span {
  font-weight: bold;
  color: #333;
  margin-right: 10px;
}

.user-info input {
  width: 60%;
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
.Pfooter{
  background-color: #2d68a894;
  color: #fff;
  padding: 10px;
  text-align: center;
  position: relative;
  width: 100%;
}
</style>