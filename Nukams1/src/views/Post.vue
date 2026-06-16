<template>
    <div class="post">
      <!-- back to last page -->
      <div class="menu">
        <button @click="$router.back()">Back</button>
        <!-- routerlink to user's self post 要改成加上vuex的狀態訊息-->
        <button v-if="!route.params.username" @click="$router.push({ name: 'post_self', params: { username: user_id } })">My Post</button>
        <button v-if="route.params.username" @click="$router.push({ name: 'addPost', params: { username: route.params.username } })">新增</button>
      </div>
      <div class="posts-page">
        <PostCard
          v-for="(post, index) in filteredPosts"
          :key="index"
          :avatar="publicAvatarPath + post.avatar"
          :image="publicPostPath+ post.image"
          :content="post.content"
          :username="post.username"
          :messages="filteredMessages(post.post_id)"
          :post_id="post.post_id"
          :user_id="post.avatar_id"
        />
      </div>
    </div>
  </template>
  
<script setup>
  import { ref, computed } from 'vue'
  import { useRoute } from 'vue-router'
  import PostCard from '../components/Postcard.vue'
  import { onMounted, onUnmounted } from 'vue'
  import axios from 'axios'
  
  const publicPostPath = '/pic/AD/'
  const publicAvatarPath = '/pic/POST/Avatar/'
  const route = useRoute()
  const posts = ref([])
  const messages = ref([])
  const user_id = localStorage.getItem('user');
  // from api get posts(post_id, posts, username, avatar, image)
  onMounted(async () => {
    try {
    const postResponse = await axios.get('http://localhost:5000/api/post');
    posts.value = postResponse.data.data;
    
  } catch (error) {
    console.error('Error fetching posts:', error);
  }

  try {
    const commentResponse = await axios.get('http://localhost:5000/api/all_comment');
    messages.value = commentResponse.data.data;
  } catch (error) {
    console.error('Error fetching comments:', error);
  }
  });
  onUnmounted(() => {
    console.log('Component unmounted')
  })
  const filteredPosts = computed(() => {
    const username = route.params.username
    if (username) {
      return posts.value.filter(post => post.avatar_id === username)
    }
    return posts.value
  })
  // function to filter messages by post_id
const filteredMessages = (postId) => {
  return messages.value.filter(message => message.post_id === postId)
}
</script>

  <style scoped>
  .post{
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    padding: 20px;
    color: black;
    min-width: 679px;
  
  }
  .posts-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    width: 90%;
    color: black;
    border: 3px rgb(213, 222, 226) solid;
    border-radius: 10px;
  }
  .menu {
    width: 10%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding: 20px;
    color: black;
    margin: 10px;
  }
  button {
        background-color:  rgb(22, 55, 69);
        color: rgb(255, 255, 255);
        font-size: large;
        font-weight: bold;
        font-family: 'Times New Roman', Times, serif;
        margin-bottom: 10px;
        border: none;
        border-radius: 30px;
        cursor: pointer;
        width: 100%;
        max-height: 56.8px;
        min-width: 70px;
        
    }
  
    button:hover {
      background-color: rgb(23, 46, 56);
      color: rgb(213, 222, 226);
    }
  </style>