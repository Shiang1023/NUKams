<template>
    <div class="login">
        <form>
            <label for="username">Account:</label>
            <input v-model="user.username" type="text" id="username" name="username" placeholder="Enter your username" required>
            <label for="password">Password:</label>
            <input v-model="user.password" type="password" id="password" name="password" placeholder="Enter your password" required>
            <button @click.prevent="login" type="submit">Login</button>
        </form>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';

const user = ref({
    username: '',
    password: '',
    type: ''
});

const router = useRouter();

// const login = () => {
//     const path = `http://localhost:5000/login/${user.username}/${user.password}`;
//     axios.get(path)
//     .then((res) => {
//         if (res.data.login.length > 0) {
//             user.type = res.data.login[0].type;
//             navigateToPage();
//         } else {
//             alert('Invalid username or password');
//         }
//     })
//     .catch((error) => {
//         console.error(error);
//         alert('Invalid username or password');
//     });
// };
const login = async () => {
    try {
        const res = await axios.post('http://localhost:5000/api/login', {
            username: user.value.username,
            password: user.value.password
        });
        if (res.data){
            console.log(res.data.data);
            user.value.type = res.data.data;
            const uid = user.value.username;
            localStorage.setItem('user', uid);
            localStorage.setItem('role', JSON.stringify(user.value.type));
            localStorage.setItem('Auth', 'true');
            navigateToPage();
        }else{
            alert('Invalid username or password');
        }
    } catch (error) {
        console.error(error);
        alert('Invalid username or password');
    }
};
    
const navigateToPage = () => {
    switch (user.value.type) {
        case '學生':
            router.push(`/STSmain/STS/${user.value.username}`);
            break;
        case '老師':
            router.push(`/TCSmain/TCS/${user.value.username}`);
            break;
        case '管理員':
            router.push(`/ADSmain/ADS/${user.value.username}`);
            break;
        case '房東':
            router.push(`/LDSmain/LDS/${user.value.username}`);
            break;
        default:
            console.error('Invalid user type');
    }
};
</script>
<style scoped>
    .login{
        display: flex;
        justify-content: center;
        font-size: large;
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
        min-height: 70vh;
        margin: auto; /* 調整上邊距以避免被固定的標題遮擋 */
    }
    form{
        width: 100%;
        display: flex;
        flex-direction: column;
        flex-wrap: wrap;
        justify-content: center;
        align-items: flex-start;
    }
    input[type=text], input[type=password] {
        max-height: 51px;
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        /* display: inline-block; */
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
        color: rgb(26, 36, 85);
    }
  
    button {
        background-color:  rgb(213, 222, 226);
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
        max-height: 56.8px;
        
    }
  
    button:hover {
      background-color: rgb(23, 46, 56);
      color: rgb(213, 222, 226);
    }
  
</style>