<template>
  <div>
    
    <main>
      <div class="repair-form">
        <h2>提交修繕報單</h2>
        <form @submit.prevent="updateUserInfo">

          <label for="student_id">學號</label>
          <input type="text" id="student_id" v-model="form.student_id" disabled >

          <label for="landlord_id">房東ID</label>
          <input type="text" id="landlord_id" v-model="form.landlord_id" disabled >

          <label for="repair_detail">修繕內容</label>
          <input type="text" id="repair_detail" v-model="form.repair_detail" required>

          <button type="submit" id="submit" style="margin-left: 100px; font-size: 20px;">提交</button>
        </form>
      </div>
    </main>
    
  </div>
</template>

<script >
import axios from 'axios';


export default {
name: 'repair_st',
data() {
return {
  form: {},
  isEditing: false,
};
},
created() {
  this.getUserInfo(this.$route.params.st_id);
},
methods: {
getUserInfo(studentId) {
  const path = `http://localhost:5000/repair/${studentId}`;
  axios.get(path)
    .then((res) => {
      this.form = res.data.repair;
      this.form.student_id = this.$route.params.st_id;
      
    })
    .catch((error) => {
      console.error(error);
    });
},

updateUserInfo() {
  
  const path = `http://localhost:5000/repair/${this.form.student_id}`;
  console.log("Updating user info with data: ", this.form); // 調試輸出
  axios.post(path, this.form)
    .then(response => {
      this.getUserInfo(this.form.student_id); // 重新獲取用戶資訊
      this.toggleEdit(); // 切換回非編輯模式
      alert("修繕報單已送出")
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
.dropdown {
  position: relative;
  display: inline-block;
}
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}
.dropdown-content a:hover {
  background-color: #f1f1f1;
}
.dropdown:hover .dropdown-content {
  display: block;
}
main {
  padding: 20px;
  flex: 1;
}
.repair-form {
  max-width: 600px;
  width: 90%;
  margin: 0px auto;
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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
.repair-form textarea {
  width: 100%;
  padding: 50px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.repair-form 
.repair-form button {
  padding: 10px 10px;
  background-color: #2d68a8;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
#submit {
  padding: 10px 20px;
  background-color: #2d68a8;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.repair-form button:hover {
  background-color: #1a4e7a;
}
#date {
    padding: 10px;
}
#name {
    padding: 10px;
}
#address {
    padding: 10px;
}
#phone {
    padding: 10px;
}
#email {
    padding: 10px;
}

</style>