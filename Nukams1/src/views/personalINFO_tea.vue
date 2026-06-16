<template>
  
    <div class="user-info">
      <h2>個人資料</h2>
      <div v-if="!isEditing">
        <p><span>姓名:</span> {{ user.name }}</p>
        <p><span>職級:</span> {{ user.position }}</p>
        <p><span>連絡電話:</span> {{ user.contactNumber }}</p>
        <p><span>Email:</span> {{ user.email }}</p>
        <p><span>辦公室位址:</span> {{ user.officeAddress }}</p>
        <p><span>辦公室電話:</span> {{ user.officePhone }}</p>
        <button type="button" @click="toggleEdit">修改</button>
      </div>
      <form v-else @submit.prevent="updateUserInfo">
        <label>姓名</label>
        <input type="text" v-model="user.name" disabled>

        <label>職級</label>
        <input type="text" v-model="user.position">

        <label>連絡電話</label>
        <input type="text" v-model="user.contactNumber">

        <label>Email</label>
        <input type="email" v-model="user.email">

        <label>辦公室位址</label>
        <input type="text" v-model="user.officeAddress">

        <label>辦公室電話</label>
        <input type="text" v-model="user.officePhone">

        <button type="submit">完成</button>
      </form>
    </div>
  
</template>

<script>
import axios from 'axios';

export default {
  name: 'personalINFO_tea',
  data() {
    return {
      user: {},
      isEditing: false,
    };
  },
  created() {
    this.getUserInfo(this.$route.params.id);
  },
  methods: {
    getUserInfo(id) {
      const path = `http://localhost:5000/TCS_info/${id}`;
      axios.get(path)
        .then((res) => {
          this.user = res.data.TCS_info;
          this.user.id = res.data.TCS_info.id; // 將 id 賦值給 this.user.id
        })
        .catch((error) => {
          console.error(error);
        });
    },

    updateUserInfo() {
      const path = `http://localhost:5000/TCS_info/${this.user.id}`;
      console.log("Updating user info with data: ", this.user); // 調試輸出
      axios.post(path, this.user)
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
  
  max-height: 550px; /* 限制最大高度 */
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
.Pfooter {
  background-color: #2d68a894;
  color: #fff;
  padding: 10px;
  text-align: center;
  position: relative;
  width: 100%;
}
</style>