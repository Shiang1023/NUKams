<template>
    <div class="register">
      <form>
          <label for="userid">Account:</label>
          <input v-model="user.userid" type="text" id="userid" name="userid" placeholder="Enter your userid(學號、教職員編號)" required>
          <label for="password">Password:</label>
          <input v-model="user.password" type="password" id="password" name="password" placeholder="Enter your password" required>
          <label for="username">Username:</label>
          <input v-model="user.username" type="text" id="username" name="username" placeholder="Enter your name" required>
          <label for="email">Email:</label>
          <input v-model="user.email" type="email" id="email" name="email" placeholder="Enter your email" required>
          <label for="phone">Phone:</label>
          <input v-model="user.phone" type="text" id="phone" name="phone" placeholder="Enter your phone" required>
          
          
          <!-- add checkbox to choose one character: teacher, student, landlord-->
          <div class="role">
            <label for="role">Role:</label>
            <div class="flex flex-row justify-between w-5/12 pl-5">
              <div>
                <label for="teacher">Teacher</label>
                <input v-model="user.role" type="radio" id="teacher" name="role" value="teacher" class="ml-2">
              </div>
              <div>
                <label for="student">Student</label>
                <input v-model="user.role" type="radio" id="student" name="role" value="student" class="ml-2">
              </div>
              <div>
                <label for="landlord">Landlord</label>
                <input v-model="user.role" type="radio" id="landlord" name="role" value="landlord" class="ml-2">
              </div>
            </div>
          </div>
          <!-- select gender -->
          <div class="gender">
            <label for="gender">Gender:</label>
            <div id="MF">
              <div class="flex flex-row justify-between w-4/12">
                <label for="male">Male</label>
                <input v-model="user.gender" type="radio" id="male" name="gender" value="male">
              </div>
              <div class="flex flex-row justify-between w-5/12">
                <label for="female">Female</label>
                <input v-model="user.gender" type="radio" id="female" name="gender" value="female">
              </div>
              
            </div>
          </div>
          
        <button @click.prevent="Register" type="submit">Register</button>
        
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  const user = ref({
      userid: '',
      username: '',
      email: '',
      phone: '',
      password: '',
      role: '',
      gender: ''
  });
  const router = useRouter();

  function togglerole(){
    if (document.getElementById('teacher').checked){
      document.getElementById('student').checked = false;
    }
    if (document.getElementById('student').checked){
      document.getElementById('teacher').checked = false;
    }
    console.log(user);
  }
  
  const Register = async () => {
      try {
          const res = await axios.post('http://localhost:5000/api/register', user.value);
          if (res.data.status === 'success'){
              console.log(res.data);
              alert('Register successfully');
              router.push({ name: 'login' });
          }
          else{
              alert('Register failed(您已註冊過帳號，請直接登入)');
          }
      } catch (error) {
          console.error(error);
          alert('Register failed');
      }
  };

  const selectRole = (selectedRole) => {
  
    if (selectedRole !== 'teacher') {
      user.role = user.role.filter(role => role !== 'teacher');
    }
    if (selectedRole !== 'student') {
      user.role = user.role.filter(role => role !== 'student');
    }
    if (selectedRole !== 'landlord') {
      user.role = user.role.filter(role => role !== 'landlord');
    }
  };
  </script>
  
  <style scoped>
  .register {
        display: flex;
        justify-content: space-between;
        font-size:medium;
        font-weight: bold;
        font-family: 'Times New Roman', Times, serif;
        background-color: #4c555f;
        color: white;
        padding: 20px;
        border-radius: 5px;
        /* box-shadow: 0 0 10px rgb(56, 57, 68); */
        width: 100%;
        max-width: 700px;
        max-height: 70vh;
        overflow: auto;
        display: flex;
        margin: auto;
    }
    form{
        width: 100%;
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: space-between;
        color: white;
    }
  
  input[type=text], input[type=email], input[type=password] {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    /* display: inline-block; */
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    color: black;
  }

  .role {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    width: 100%;
  }
  
  button {
    background-color: rgb(213, 222, 226);
    color: rgb(26, 36, 85);
    font-size: large;
    font-weight: bold;
    font-family: 'Times New Roman', Times, serif;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    width: 100%;
  }
  
  button:hover {
    background-color: rgb(23, 46, 56);
    color: rgb(213, 222, 226);
  }
  .gender {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 40%;
  }
  #MF {
    padding: 0 20px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 80%;
  }
  </style>