<template>
    <div class="comment">
      <!-- back to last page -->
        <div class="menu">
            <button @click="$router.back()">Back</button>
            <!-- routerlink to user's self post -->
        </div>
        <div class="comm-page">
                <comment
                v-for="(Comm, index) in Comms"
                :key="index"
                :image="publicPostPath+Comm.picture"
                :address="Comm.address"
                :phone="landlord.phone"
                :title="Comm.build_type"
                :username="$route.params.username"
                :messages="filteredMessages(Comm.rent_id)"
                :comment_id="Comm.rent_id"


                />
        </div>
        
    </div>
  </template>
  
<script setup>


    import { ref, computed, onMounted } from 'vue'
    import { useRoute } from 'vue-router'
    import comment from '../components/comment.vue'
    import axios from 'axios'
    
    const route = useRoute()
    const publicPostPath = '/pic/AD/'
    const Comms = ref([])
    const messages = ref([])
    const landlord = ref('')
    // from api get posts(post_id, posts, username, avatar, image)
    onMounted(async () => {
        try {
          const commentResponse = await axios.get('http://localhost:5000/api/get_rent_info');
          Comms.value = commentResponse.data.data;
        } catch (error) {
         console.error('Error fetching comments:', error);
        }
        try {
          const path = `http://localhost:5000/api/get_landlord_phone/${Comms.value[0].landlord_id}`;
          const commentResponse = await axios.get(path);
          landlord.value = commentResponse.data.landlord_phone;
        } catch (error) {
          console.error('Error fetching comments:', error);
        }
        try {
          const commentResponse = await axios.get('http://localhost:5000/api/all_rent_comment');
          messages.value = commentResponse.data.data;
        } catch (error) {
          console.error('Error fetching comments:', error);
        }
    });
    const filteredMessages = (rentid) => {
      return messages.value.filter(message => message.rent_id === rentid)
    }  
</script>

  <style scoped>
  .comment{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: flex-start;
    padding: 20px;
    color: black;
    min-width: 679px;
  
  }
  .comm-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    width: 90%;
    color: black;
  }
  .menu {
    width: 10%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding: 20px;
    color: black;
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
        
    }
  
    button:hover {
      background-color: rgb(23, 46, 56);
      color: rgb(213, 222, 226);
    }
  </style>