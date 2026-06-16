<template>
  <div class="wrapper">
    <nav>
      <aside>
        <router-link to="VertifyManager_ad">廣告</router-link>
        <router-link to="VertifyManager_post">貼文</router-link>
        <router-link to="VertifyManager_comment">留言</router-link>
      </aside>
    </nav>
    <main>
      <div v-for="comment in comments" :key="comment.id" class="button-container">
        <div class="button">
          {{ comment.comment_id }}-{{ comment.post_id }} : {{ comment.comment_detail }}
          <div class="delete-button" @click="confirmDelete(comment.comment_id)">刪除</div>
          <div class="confirm-button" @click="confirmVerified(comment.comment_id)">確認</div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'VertifyManager_comment',
  data() {
    return {
      comments: [],
    };
  },
  created() {
    this.getComments();
  },
  methods: {
    getComments() {
      const path = 'http://127.0.0.1:5000/api/reported_comment';
      axios.get(path)
        .then((res) => {
          this.comments = res.data.comment_report;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    deleteComment(commentId) {
      const deletePath = `http://127.0.0.1:5000/api/delete_comment/${commentId}`;
      axios.get(deletePath)
        .then((res) => {
          console.log('Comment deleted successfully:', res.data);
          this.getComments(); // Refresh comments after deletion
        })
        .catch((error) => {
          console.error('Error deleting comment:', error);
        });
    },
    verifyComment(commentId) {
      const verifyPath = `http://127.0.0.1:5000/api/make_report_0/${commentId},comment`;
      axios.get(verifyPath)
        .then((res) => {
          console.log('Comment verified successfully:', res.data);
          this.getComments(); // Refresh comments after verification
        })
        .catch((error) => {
          console.error('Error verifying comment:', error);
        });
    },
    confirmDelete(commentId) {
      if (window.confirm('確定要刪除這條留言嗎？')) {
        this.deleteComment(commentId);
      }
    },
    confirmVerified(commentId) {
      if (window.confirm('確定要確認這條留言嗎？')) {
        this.verifyComment(commentId);
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

.confirm-button,
.delete-button {
  position: absolute;
  top: 0;
  width: 50px;
  background-color: green;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.delete-button {
  right: 0;
  background-color: red;
}

.confirm-button {
  right: 55px;
}

.confirm-button:hover,
.delete-button:hover {
  background-color: darkgreen;
}
</style>
