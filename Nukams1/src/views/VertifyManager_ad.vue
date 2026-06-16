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
      <div v-for="ad in advertisements" :key="ad.id" class="button-container">
        <div class="button">
          {{ ad.repair_id }} {{ ad.repair_descrition }}
          <div class="delete-button" @click="confirmDelete(ad.repair_id)">刪除</div>
          <div class="confirm-button" @click="confirmVerified(ad.repair_id)">確認</div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'VertifyManager_ad',
  data() {
    return {
      advertisements: [],
    };
  },
  created() {
    this.getAdvertisements();
  },
  methods: {
    getAdvertisements() {
      const path = 'http://127.0.0.1:5000/api/reported_advertisement';
      axios.get(path)
        .then((res) => {
          this.advertisements = res.data.ad_report;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    deleteAdvertisement(adId) {
      const deletePath = `http://127.0.0.1:5000/api/delete_advertisement/${adId}`;
      axios.get(deletePath)
        .then((res) => {
          console.log('Advertisement deleted successfully:', res.data);
          this.getAdvertisements(); // Refresh advertisements after deletion
        })
        .catch((error) => {
          console.error('Error deleting advertisement:', error);
        });
    },
    verifyAdvertisement(adId) {
      const verifyPath = `http://127.0.0.1:5000/api/make_report_0/${adId},advertisement`;
      axios.get(verifyPath)
        .then((res) => {
          console.log('Advertisement verified successfully:', res.data);
          this.getAdvertisements(); // Refresh advertisements after verification
        })
        .catch((error) => {
          console.error('Error verifying advertisement:', error);
        });
    },
    confirmDelete(adId) {
      if (window.confirm('確定要刪除這條廣告嗎？')) {
        this.deleteAdvertisement(adId);
      }
    },
    confirmVerified(adId) {
      if (window.confirm('確定要確認這條廣告嗎？')) {
        this.verifyAdvertisement(adId);
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
