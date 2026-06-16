<template>
    <div class="accst">
      
      
        <div class="repair-form">
          <h2>校外住宿資料</h2>
          <form @submit.prevent="updateUserInfo">
            <label for="studentId">學號</label>
            <input type="text" id="studentId" v-model="form.studentId" :readonly="!isEditing" required>
  
            <label for="address">住宿地址</label>
            <input type="text" id="address" v-model="form.address" :readonly="!isEditing" required>
  
            <label for="roommates">同住室友</label>
            <input type="text" id="roommates" v-model="form.roomates" :readonly="!isEditing" required>
  
            <label for="landlordName">房東姓名</label>
            <input type="text" id="landlordName" v-model="form.landlordName" :readonly="!isEditing" required>
  
            <label for="landlordPhone">房東電話</label>
            <input type="text" id="landlordPhone" v-model="form.landlordPhone" :readonly="!isEditing" required>
  
            <label for="rent">月租</label>
            <input type="text" id="rent" v-model="form.rent" :readonly="!isEditing" required>
  
            <label for="academicYear">學年</label>
            <select id="academicYear" v-model="form.academicYear" :disabled="!isEditing" required>
              <option value="">選擇學年</option>
              <option value="112">112</option>
              <option value="113">113</option>
              <option value="114">114</option>
            </select>
  
            <label for="semaster">學期</label>
            <select id="semaster" v-model="form.semaster" :disabled="!isEditing" required>
              <option value="">選擇學期</option>
              <option value="1">第一學期</option>
              <option value="2">第二學期</option>
            </select>
  
            <button type="button" @click="toggleEdit" v-if="!isEditing">修改</button>
            <button type="submit" v-if="isEditing">完成</button>
          </form>
        </div>
     
      
    </div>
  </template>
  
  <script >
  import App from '@/App.vue';
import axios from 'axios';


export default {
name: 'Accommodation_st',
data() {
  return {
    form: {},
    isEditing: false,
  };
},
created() {
  this.getUserInfo(this.$route.params.studentId,this.$route.params.academicYear,this.$route.params.semaster);
},
methods: {
  getUserInfo(studentId,academicYear,semaster) {
    const path = `http://localhost:5000/accommodation_st/${studentId}/${academicYear}/${semaster}`;
    axios.get(path)
      .then((res) => {
        this.form = res.data.accommodation_st;
        this.form.studentId = res.data.accommodation_st.studentId; // 將 id 賦值給 this.user.id
        this.form.academicYear = res.data.accommodation_st.academicYear;
        this.form.semester = res.data.accommodation_st.semaster;
      })
      .catch((error) => {
        console.error(error);
      });
      console.log("Getting user info with data: ", this.form.studentId);
  },

  updateUserInfo() {
    const path = `http://localhost:5000/accommodation_st/${this.form.studentId}/${this.form.academicYear}/${this.form.semaster}`;
    console.log("Updating user info with data: ", this.user); // 調試輸出
    axios.post(path, this.form)
      .then(response => {
        this.getUserInfo(this.form.studentId,this.form.academicYear,this.form.semaster); // 重新獲取用戶資訊
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
  main {
    padding: 20px;
    flex: 1;
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
  .repair-form {
    max-width: 600px;
    margin: 0 auto;
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-height: 530px; 
    overflow-y: auto; 
  }
  .repair-form h2 {
    text-align: center;
    color: #333;
  }
  .repair-form label {
    display: block;
    margin: 10px 0 5px;
    font-weight: bold;
    color: #333;
  }
  .repair-form input,
  .repair-form textarea,
  .repair-form select {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  .repair-form input[readonly],
  .repair-form textarea[readonly],
  .repair-form select[disabled] {
    background-color: #eee;
    cursor: not-allowed;
  }
  .repair-form button {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #2d68a894;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 10px;
  }
  .repair-form button:hover {
    background-color: #1a4e7a;
  }
  .accst{
    width: 100%;
  }
  
  
  </style>
  