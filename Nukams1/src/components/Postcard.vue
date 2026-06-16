<template>
  <div class="post-card">
    <div class="post-header">
      <div class="HeaderLeft">
        <img :src="avatar" alt="Avatar" class="avatar" />
        <div class="username">{{ username }}</div>
      </div>
      <button v-if="InPost" @click="report" class="report">檢舉</button>
    </div>
    <div class="post-image">
      <img :src="image" alt="Post Image" />
    </div>
    <div class="post-content">
      <p v-if="!isEditing">{{ content }}</p>
      <div v-if="isEditing" class="edit-container">
        <input type="text" v-model="newContent" class="edit-input" />
        <div class="edit-buttons">
          <button @click="saveContent" class="save-button">保存</button>
          <button @click="cancelEdit" class="cancel-button">取消</button>
        </div>
      </div>
    </div>
    <div v-if="!isUserPost" class="message">
      <input type="text" v-model="message" placeholder="輸入留言..." />
      <button @click.prevent="addMessage">留言</button>
    </div>
    <button v-if="isUserPost && !isEditing" @click="editPost" id="modify">修改</button>
    <button v-if="isUserPost" @click="deletePost" id="delete">刪除</button>
    <button @click="toggleMessages">{{ showMessages ? '隱藏留言' : '顯示留言' }}</button>
  </div>
  <div v-if="showMessages && messages.length > 0" class="messages">
    <div v-for="(message, index) in messages" :key="index" class="message">
      <div class="flex flex-row items-center w-10/12 overflow-auto">
        <img :src="publicPath + message.avatar" alt="Avatar" class="avatar" />
        <p class="font-bold mr-2">{{ message.username }}</p>
        <p v-if="!message.isEditing">{{ message.content }}</p>
        <div v-if="message.isEditing" class="edit-container">
          <input type="text" v-model="message.newContent" class="edit-input" />
          <div class="edit-buttons">
            <button @click="saveMessage(message, index)" class="save-button">保存</button>
            <button @click="cancelMessageEdit(message)" class="cancel-button">取消</button>
          </div>
        </div>
      </div>
      <div class="mod">
        <button v-if="message.id === user_id" @click.prevent="deleteMessage(message)">刪除</button>
        <button v-if="message.id === user_id" @click.prevent="editMessage(message)">修改</button>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, computed } from 'vue'
import { defineProps } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios';

const props = defineProps({
  avatar: {
    type: String,
    required: true,
  },
  image: {
    type: String,
    required: true,
  },
  content: {
    type: String,
    required: true,
  },
  username: {
    type: String,
    default: '使用者名稱',
  },
  messages: {
    type: Array,
    default: () => [],
  },
  post_id: {
    type: String,
    default: 1,
  },
  user_id: {
    type: String,
    default: 'A1105503',
  },
})

const route = useRoute()
const publicPath = '/pic/POST/Avatar/'
const message = ref('')
const showMessages = ref(false)
const InPost = route.name === 'post'
const isUserPost = computed(() => {
  return route.params.username === props.user_id
})
const user_id = localStorage.getItem('user')
const isEditing = ref(false)
const newContent = ref(props.content)

const addMessage = async () => {
  if (message.value.trim() !== '') {
    try {
      // 發送 POST 請求到後端
      const res = await axios.post('http://localhost:5000/api/insert_comment_two', {
        post_id: props.post_id, // 對應的 post_id
        user_id: user_id, // 使用者ID，這裡需要替換成實際的使用者ID
        content: message.value,
      });

      // 假設後端回應包含 avatar_picture
      const avatarPicture = res.data.avatar_picture;
      const username = res.data.username;
      // 更新本地消息列表
      props.messages.push({ content: message.value, username:username,avatar: avatarPicture });

      // 清空輸入框
      message.value = '';
      
    } catch (error) {
      console.error("Error adding message:", error)
      alert('Failed to add message. Please try again.')
    }
  }
};

const editPost = () => {
  isEditing.value = true
}

const saveContent = async () => {
  try {

    const response = await axios.get(`http://localhost:5000/api/update_post/${props.post_id},${newContent.value}`, {
      content: newContent.value
    })
    if (response.status === 200) {
      props.content = newContent.value
      isEditing.value = false
      alert('Post has been updated successfully!')
    }
  } catch (error) {
    console.error("Error updating post:", error)
    alert('Failed to update the post. Please try again.')
  }
  window.location.reload()
}

const cancelEdit = () => {
  isEditing.value = false
  newContent.value = props.content
}

const deletePost = async () => {
  if (confirm("你確定要刪除此貼文嗎?")) {
    try {
      const response = await axios.get(`http://localhost:5000/api/delete_post/${props.post_id}`)
      if (response.status === 200) {
        alert('Post has been deleted successfully!')
        // Optionally, you can redirect the user or update the UI after successful deletion
      }
    } catch (error) {
      console.error("Error deleting post:", error)
      alert('Failed to delete the post. Please try again.')
    }
  }
  window.location.reload()
}

const toggleMessages = () => {
  showMessages.value = !showMessages.value
}

function report() {
    alert('檢舉成功')
    const path = `http://127.0.0.1:5000/api/update_report_to_one/${props.p_id},post`;
    console.log(path)
    axios.get(path)
      .then((res) => {
        console.log("succeed");
      })
      .catch((error) => {
        console.error(error);
      });
    }

const deleteMessage =(message)=> {
  if (confirm("你確定要刪除此留言嗎?")) {
    try {
      const response = axios.get(`http://localhost:5000/api/delete_comment/${message.comment_id
}`)
      if (response.status === 200) {
        alert('Message has been deleted successfully!')
        // Optionally, you can redirect the user or update the UI after successful deletion
      }
    } catch (error) {
      console.error("Error deleting Message:", error)
      alert('Failed to delete the Message. Please try again.')
    }
  }
  window.location.reload()
}

const editMessage = (message) => {
  message.isEditing = true
  message.newContent = message.content
}

const saveMessage = async (message, index) => {
  try {
    const response = await axios.get(`http://localhost:5000/api/update_comment/${message.comment_id
},${message.newContent}`)
    if (response.status === 200) {
      message.content = message.newContent
      message.isEditing = false
      alert('Message has been updated successfully!')
    }
  } catch (error) {
    console.error("Error updating message:", error)
    alert('Failed to update the message. Please try again.')
  }
  
}

const cancelMessageEdit = (message) => {
  message.isEditing = false
  message.newContent = message.content
}
</script>


<style scoped>
.post-card {
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.537);
  overflow: hidden;
  margin-bottom: 10px;
  width: 60%;
  max-width: 700px;
  background-color: rgb(215, 219, 225);
  min-width: 380px;
}

.post-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 10px;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}

.username {
  font-weight: bold;
}

.post-image {
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  height: 300px; /* 設置圖片框的高度 */
  background-color: #dde9f6;
}

.post-image img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain; /* 確保圖片等比例縮小以適應容器 */
}

.post-content {
  padding: 10px;
}

.edit-container {
  display: flex;
  align-items: center;
  padding: 10px;
}

.edit-input {
  flex: 1;
  padding: 8px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1em;
}

.edit-buttons {
  display: flex;
  align-items: center;
}

.save-button {
  padding: 8px 16px;
  margin: 5px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1em;
}
.cancel-button{

  padding: 8px 16px;
  margin: 5px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1em;
  

}

.save-button {
  background-color: #4caf50;
  color: white;
}

.save-button:hover {
  background-color: #45a049;
}

.cancel-button {
  background-color: #f44336;
  color: white;
}

.cancel-button:hover {
  background-color: #da190b;
}

.message {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px;
  background-color: rgb(215, 219, 225);
  width: 100%;
}

.message input {
  flex: 1;
  padding: 5px;
  margin-right: 10px;
}

.message button {
  padding: 5px 10px;
  background-color: #b2cff1;
}

.message button:hover {
  background-color: #8db0d9;
}

.toggle-button {
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  width: 100%;
  text-align: center;
}

.toggle-button:hover {
  background-color: #0056b3;
}

.messages {
  margin: 10px;
  width: 60%;
  max-width: 700px;
  background-color: #f9f9f9;
  border-top: 1px solid #ccc;
}

.messages .message {
  padding: 5px 0;
}

#modify {
  background-color: #f4c96c;
  color: rgb(0, 0, 0);
  border: none;
  cursor: pointer;
  width: 100%;
  text-align: center;
}

#modify:hover {
  background-color: #bf9d36;
  color: #ffffff;
}

#delete {
  background-color: #f86e9a;
  color: black;
  border: none;
  cursor: pointer;
  width: 100%;
  text-align: center;
}

#delete:hover {
  background-color: #d03655;
  color: white;
}

.report {
  background-color: #fa761e98;
  color: white;
  font-size: 1em;
  font-weight: bold;
  font-family: 'Times New Roman', Times, serif;
  padding: 5px 10px;
  border: none;
  border-radius: 30px;
  cursor: pointer;
}

.HeaderLeft {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.post-header button:hover {
  background-color: #b46936;
  color: white;
}
</style>