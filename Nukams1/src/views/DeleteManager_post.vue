<template>
  <div class="wrapper">
    <nav>
      <aside>
        <router-link to="DeleteManager_ad">廣告</router-link>
        <router-link to="DeleteManager_post">貼文</router-link>
        <router-link to="DeleteManager_comment">留言</router-link>
      </aside>
    </nav>
    <main>
      <div v-for="post in posts" :key="post.post_id" class="button-container">
        <div class="button">
          {{ post.post_id }}
          <div class="delete-button" @click="confirmDelete(post.post_id)">刪除</div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'DeleteManager_post',
  data() {
    return {
      posts: [],
    };
  },
  created() {
    this.getPosts();
  },
  methods: {
    getPosts() {
      const path = 'http://127.0.0.1:5000/api/post/get_all_post';
      axios.get(path)
        .then((res) => {
          this.posts = res.data.post_info;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    DeletePost(postId) {
      const deletePath = `http://127.0.0.1:5000/api/delete_post/${postId}`;
      axios.get(deletePath)
        .then((res) => {
          console.log('Post deleted successfully:', res.data);
          this.getPosts(); // Refresh posts after deletion
        })
        .catch((error) => {
          console.error('Error deleting post:', error);
        });
    },
    confirmDelete(postId) {
      if (window.confirm('確定要刪除這篇貼文嗎？')) {
        this.DeletePost(postId);
      } else {
        // User clicked cancel, do nothing
      }
    },
  },
};
</script>

<style scoped>
.wrapper {
  display: flex;
}

nav {
  position: fixed;
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  padding-left: 200px;
}

aside {
  background-color: #f1f1f1;
  width: 100px;
  padding: 10px;
  box-shadow: 2px 0 5px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
}

aside a {
  display: block;
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  background-color: #2d68a894;
  color: white;
  font-size: 16px;
  text-align: center;
  text-decoration: none;
}

aside a:hover {
  background-color: #1a4e7a;
}

main {
  margin-left: 120px;
  flex-grow: 1;
}

.button-container {
  text-align: center;
  position: relative;
  margin-bottom: 10px;
}

.button {
  position: relative;
  width: 600px;
  background-color: #2d68a894;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
  transition: background-color 0.3s;
  text-align: left;
}

.delete-button {
  position: absolute;
  top: 0;
  right: 0;
  width: 50px;
  background-color: red;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.delete-button:hover {
  background-color: darkred;
}
</style>
