<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Up from '../components/Up.vue'
import Down from '../components/Down.vue'
</script>

<template>
    <Up />
    <div class="body">
      <div class="login-container">
        <div class="link">
          <RouterLink to="login" class="button" style="display: flex; justify-content: center; padding: 0 5%;">Login</RouterLink>
          <RouterLink to="register" class="button" style="display: flex; justify-content: center;padding:0 5%;">Register</RouterLink>
        </div> 
        <RouterView />
      </div>
    </div>
    <Down />
</template>
  
<style scoped>
    .body{
      width: 100%;
      height: 100%;
      display: flex;
      flex-wrap: wrap;
      flex-direction: column;
      justify-content: space-between;
      align-items: stretch;
      background-color: rgb(145, 186, 219);
      overflow: hidden;
    }
    .login-container {
      display: flex;
      justify-content: space-around;
      flex-direction: column;
      text-align: center;
      font-size: large;
      font-weight: bold;
      font-family: 'Times New Roman', Times, serif;
      background-color: #4c555f;
      color: white;
      padding: 10px;
      border-radius: 5px;
      box-shadow: 0 0 10px rgb(56, 57, 68);
      width: 100%;
      height: 80vh;
      max-width: 700px;
      margin: 1% auto;
    }
    .link{
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      padding: 0 5%;
    }

    .button{
      font-size: 20px;
      font-weight: bolder;
      background-color: #4c555f;
      color: white;
      border: none;
      border-radius: 5px;
      padding: 10px;
      margin: 10px;
      cursor: pointer;
      text-decoration: none;
    }
    .button:hover{
      background-color: #3e444c;
    }
    
</style>

