<template>
  <div id="app">
    <div class="user-info">
      <h2>個人資料</h2>
      <div v-if="!isEditing">
        <p><span>姓名:</span> {{ user.name }}</p>
        <p><span>Email:</span> {{ user.email }}</p>
        <p><span>成績:</span> {{ user.grade }}</p>
        <p><span>性別:</span> {{ genderText }}</p>
        <p><span>連絡電話:</span> {{ user.phone }}</p>
        <p><span>住址:</span> {{ user.home_address }}</p>
        <p><span>家裡電話:</span> {{ user.home_phone }}</p>
        <p><span>聯絡人:</span> {{ user.home_contact }}</p>
        <button type="button" @click="toggleEdit">修改</button>
      </div>
      <form v-else @submit.prevent="updateUserInfo">
        <label>姓名</label>
        <input type="text" v-model="user.name" disabled>

        <label>Email</label>
        <input type="text" v-model="user.email">

        <label>成績</label>
        <input type="text" v-model="user.grade">

        <label>性別</label>
        <input type="text" v-model="genderText" disabled>

        <label>連絡電話</label>
        <input type="text" v-model="user.phone">

        <label>住址</label>
        <input type="text" v-model="user.home_address">

        <label>家裡電話</label>
        <input type="text" v-model="user.home_phone">

        <label>聯絡人</label>
        <input type="text" v-model="user.home_contact">

        <button type="submit">完成</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'personalINFO_student',
  data() {
    return {
      user: {},
      isEditing: false,
      pid: this.$route.params.id
    };
  },
  created() {
    this.getUserInfo(this.$route.params.id);
    console.log(this.$route.params.id);
  },
  computed: {
    genderText() {
      return this.user.gender === '0' ? '女性' : '男性';
    }
  },
  methods: {
    getUserInfo(id) {
      const path = `http://127.0.0.1:5000/api/student/student_information/${id}`;
      console.log(path);
      axios.get(path)
        .then((res) => {
          this.user = res.data.student_information[0];
          console.log(this.user);
        })
        .catch((error) => {
          console.error(error);
        });
    },

    updateUserInfo() {
      const path = `http://127.0.0.1:5000/api/student/student_modify_information/${this.user.id},${this.user.name},${this.user.email},${this.user.grade},${this.user.phone},${this.user.home_address},${this.user.home_phone},${this.user.home_contact}`;
      console.log("Updating user info with data: ", this.user); // 調試輸出
      axios.get(path, this.user)
        .then(response => {
          this.getUserInfo(this.user.id); // 重新獲取用戶資訊
          this.toggleEdit(); // 切換回非編輯模式
        })
        .catch(error => {
          console.error(error);
        });
    },
    toggleEdit() {
      this.isEditing = !this.isEditing;
    }
  },
};
</script>

<style scoped>
.user-info {
  max-width: 600px;
  margin: 0 auto;
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: left;
  margin-top: 50px;
  margin-bottom: 100px;
}

.user-info h2 {
  text-align: center;
  color: #333;
}

.user-info p,
.user-info input,
.user-info select {
  font-size: 18px;
  line-height: 1.6;
  color: #555;
  margin: 10px 0;
}

.user-info p span {
  font-weight: bold;
  color: #333;
}

.user-info input,
.user-info select {
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
.Pfooter {
  background-color: #2d68a894;
  color: #fff;
  padding: 10px;
  text-align: center;
  position: relative;
  width: 100%;
}
</style>
