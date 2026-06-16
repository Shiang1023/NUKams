<template>
  <div class="vtst">     
      <div id="app" class="visit-form">
        <h2>填寫訪視日期</h2>
        <form @submit.prevent="updateUserInfo">
          <label for="studentId">學號</label>
          <input type="text" id="studentId" v-model="form.studentId" :readonly="!isEditing" required>

          <label for="name">姓名</label>
          <input type="text" id="name" v-model="form.name" :readonly="!isEditing" required>

          <label for="address">地址</label>
          <input type="text" id="address" v-model="form.address" :readonly="!isEditing" required>

          <label for="visit-date">可訪視日期</label>
          <input type="date" id="visit-date" v-model="form.available_time" :readonly="!isEditing" required>

          <button type="button" @click="toggleEdit" v-if="!isEditing">修改</button>
          <button type="submit" v-if="isEditing">完成</button>
          
        </form>
      </div>
  </div>
</template>

<script >
import axios from 'axios';


export default {
name: 'visittime_st',
data() {
return {
  form: {},
  isEditing: false,
};
},
created() {
this.getUserInfo(this.$route.params.studentId);
},
methods: {
getUserInfo(studentId) {
  const path = `http://localhost:5000/visittime_st/${studentId}`;
  axios.get(path)
    .then((res) => {
      this.form = res.data.visittime_st;
      this.form.studentId = res.data.visittime_st.studentId;
      this.form.name = res.data.visittime_st.name; // 將 id 賦值給 this.user.id
      this.form.address = res.data.visittime_st.address;
      this.form.available_time = res.data.visittime_st.available_time;
    })
    .catch((error) => {
      console.error(error);
    });
},

updateUserInfo() {
  
  const path = `http://localhost:5000/visittime_st/${this.form.studentId}`;
  console.log("Updating user info with data: ", this.form); // 調試輸出
  axios.post(path, this.form)
    .then(response => {
      this.getUserInfo(this.form.studentId); // 重新獲取用戶資訊
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
.visit-form {
max-width: 600px;
margin: 0 auto;
background-color: #f9f9f9;
padding: 25px;
border-radius: 10px;
box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
width: 100%;
max-height: 530px; 
overflow-y: auto; 
}
.visit-form h2 {
text-align: center;
color: #333;
font-size: 1.5em;
}
.visit-form label {
display: block;
margin: 5px 0 5px;
font-weight: bold;
color: #333;
font-size: 0.9em;
margin-left: 10px;
}
.visit-form input,
.visit-form select {
width: 90%;
padding: 8px;
margin-bottom: 10px;
margin-left:10px ;
border: 1px solid #ccc;
border-radius: 5px;
font-size: 0.9em;
}
.visit-form button {
display: block;
width: 50%;
padding: 8px;
margin: 0 auto;
background-color: #2d68a894;
color: #fff;
border: none;
border-radius: 5px;
cursor: pointer;
font-size: 0.9em;
}
.visit-form button:hover {
background-color: #1a4e7a;
}

.vtst{
width: 100%;
}

</style>
