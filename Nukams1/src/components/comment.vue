
<template>
    <Card class="rental-card">
        <template #header>
            <h2>{{ title }}</h2>
        </template>
        <template #content>
            <div class="rental-content">
                <img :src="image" alt="Rental Image" class="rental-image" />
                <div class="rental-details">
                    <p>評分: {{ averageRating }}</p>
                    <p>地址: {{ address }}</p>
                    <p>房東電話: {{ phone }}</p>
                </div>
            </div>
        </template>
    </Card>
    <div v-if="!isUserPost" class="message">
        <input type="text" v-model="message" placeholder="輸入留言..." />
        <div class="rating">
          <span 
            v-for="star in 5" 
            :key="star" 
            :class="{'active': star <= rating}" 
            @click="setRating(star)"
          >
            &#9733;
          </span>
        </div>
        <button @click.prevent="addMessage">留言</button>
    </div>
      
    <button v-if="isUserPost" @click="$router.push({ name: 'post_self', params: { username: username } })" id="modify">修改</button>
    <button v-if="isUserPost" @click="$router.push({ name: 'post_self', params: { username: username } })" id="delete">刪除</button>
    <button @click="toggleMessages">{{ showMessages ? '隱藏評論' : '顯示評論' }}</button>

    <div v-if="showMessages && messages.length > 0" class="messages">
      <div v-for="(message, index) in messages" :key="index" class="message">
        <div class="flex flex-row items-start h-full">
          <img :src="publicPath+ message.avatar" alt="Avatar" class="avatar" />
          <div class="h-full flex flex-col justify-start overflow-auto">
            <p class="font-bold">評分: {{ message.rating }}</p>
            <p v-if="!message.isEditing" class="font-bold  h-4/6 max-w-5xl" >{{ message.content }}</p>
            

                
          </div>
          <div v-if="message.isEditing" class="edit-container">
            <input type="text" v-model="message.newContent" class="edit-input">
          <div class="edit-button">
            <button @click="saveMessage(message,index)" class="save-button">保存</button>
            <button @click="cancelMessageEdit(message)" class="cancel-button">取消</button>
          </div>
        </div>
        
        <div class="mod">
          <button v-if="myself(index)" @click="deleteMessage(index)">刪除</button>
          <button v-if="myself(index)" @click="editMessage(message)">修改</button>
        </div>
      </div>
    </div>
  </div>

</template>
<script setup>
  import { ref ,computed, toRef } from 'vue'
  import { useRoute } from 'vue-router'
  import Card from './card.vue'
  import axios from 'axios'

  const props = defineProps({
    image: {
      type: String,
      required: true,
    },
    address: {
      type: String,
      required: true,
    },
    phone: {
      type: String,
      default: 0,
    },
    title: {
      type: String,
      required: true,
    },
    username: {
      type: String,
      required: true,
    },
    messages:{
      type: Array,
      default: () => [],
    },
    comment_id: {
      type: String,
      default: 1,
    }
  })
  console.log(props.phone)
  const message = ref('')
  const rating = ref(1)
  const Message = ref(props.messages)
  const showMessages = ref(false)
  const publicPath = '/pic/POST/Avatar/'
  const route = useRoute()
  const fetchMessages = () => {
    axios.get('http://localhost:5000/api/all_rent_comment') // Replace with your actual endpoint
        .then((res) => {
            messages.value = res.data.messages
        })
        .catch((error) => {
            console.error(error)
        })
}
  const addMessage = async () => {
    if (message.value.trim() !== '' && rating.value >= 1 && rating.value <= 5) {
      try {
      // 發送 POST 請求到後端
      const res = await axios.post('http://localhost:5000/api/insert_rent_comment', {
        rent_id: props.comment_id, // 對應的 post_id
        user_id: route.params.username, // 使用者ID，這裡需要替換成實際的使用者ID
        content: message.value,
        rating: rating.value,
      });

      // 假設後端回應包含 avatar_picture
      const avatarPicture = res.data.avatar_picture;
      const username = res.data.username;
      // 更新本地消息列表
      props.messages.push({ content: message.value, username:username,avatar: avatarPicture, rating: rating.value});
      message.value = ''
      rating.value = 1
      window.location.reload();
    } catch (error) {
      console.error('Error adding message:', error);
    }
    }
  }
  const averageRating = computed(() => {
    if (!props.messages || props.messages.length === 0) {
      return '無評分';
    }
    
    const total = props.messages.reduce((sum, message) => sum + message.rating, 0);
    const average = total / props.messages.length;
    return average.toFixed(1);
  });
  
  const toggleMessages = () => {
    showMessages.value = !showMessages.value
  }

  const setRating = (value) => {
    console.log(value)
    rating.value = value
  }

  const myself = (index) => {
    // params與存在本地的使用者名稱或ID
    return useRoute().params.username === props.messages[index].user_id
  }
  const deleteMessage = (index) => {
    const messageToDelete = props.messages[index];
    const comment_id = messageToDelete.comment_id; // Assuming comment_id is part of the message object
    const path = `http://localhost:5000/api/delete_rent_comment/${comment_id}`;

    axios.get(path)
      .then((res) => {
        if (res.data.status === 'success') {
          alert('刪除成功');
          props.messages.splice(index, 1); // Remove the message from messages array
          window.location.reload();
        } else {
          alert('刪除失敗');
        }
      })
      .catch((error) => {
        console.error(error);
        alert('刪除失敗');
      });
  };

  const editMessage = (message) => {
    message.isEditing = true;
    message.newContent = message.content;
  };

  const saveMessage = (message) => {
  try {
    const path = `http://localhost:5000/api/update_rent_comment/${message.comment_id}`;
    axios.post(path, { content: message.newContent })
      .then((res) => {
        if (res.data.status === 'success') {
          alert('修改成功');
          message.content = message.newContent;
          message.isEditing = false;
        } else {
          alert('修改失敗');
        }
      })
      .catch((error) => {
        console.error(error);
        alert('修改失敗');
      });
  } catch (error) {
    console.error(error);
  }
}


   const cancelMessageEdit = (message) => {
    message.isEditing = false;
    message.newContent = message.content;
  };
  

</script>
  
<style scoped>
  .rental-card {
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    width: 100%;
    background-color: #ffffff;
  }
  
  .rental-content {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    gap: 20px;
  }
  
  .rental-image {
    width: 300px;
    height: 200px;
    object-fit: cover;
    border-radius: 8px;
  }
  
  .rental-details {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 60%;
    /* 字體大小 */
    font-size: 1.2em;
  }
  .message {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px;
    background-color: rgb(215, 219, 225);
    width: 100%;
    height: 100px;
  }
  .message p{
    padding: 0 15px;
  }
  .message input {
    flex: 1;
    padding: 5px;
    margin-right: 10px;
  }
  
  .message button {
    padding: 5px 10px;
    background-color: #b2cff1;
    margin: 0 10px;
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
    width: 100%;
    background-color: #f9f9f9;
    border-top: 1px solid #ccc;
    display: flex;
    justify-content: center;
    flex-direction: column;
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

  .rating {
  display: flex;
  gap: 5px;
  cursor: pointer;
}

  .rating span {
    font-size: 1.5em;
    color: #ccc;
  }

  .rating span.active {
    color: #e6bf23;
  }
  .avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}
</style>