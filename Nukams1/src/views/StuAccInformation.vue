<template>
  <div id="app">
    
    <main>
  <div class="user-info">
    <h2>學生住宿資料</h2>
    <div v-if="!isEditing">
      <p><span>學號:</span> {{ user.studentId }}</p>
      <p><span>姓名:</span> {{ user.name }}</p>
      <p><span>住宿地址:</span> {{ user.address }}</p>
      <p><span>學年:</span> {{ user.academicYear }}</p>
      <p><span>學期:</span> {{ user.semaster }}</p>
      <p><span>房東姓名:</span> {{ user.landlordName }}</p>
      <p><span>房東連絡電話:</span> {{ user.landlordPhone }}</p>
      <p><span>月租:</span> {{ user.rent }}</p>
      <p><span>同住室友:</span> {{ user.roomates }}</p>
    </div>
  </div>
</main>
    
  </div>
</template>
<script setup>
import axios from 'axios';
</script>
<script>
export default {
  name: 'StuAccInformation',
  data() {
    return {
      isEditing: false,
      user: {}
    };
  },
  created() {
    this.getUserInfo(this.$route.params.id, this.$route.params.grade, this.$route.params.semester);
    
  },
  methods: {
    toggleEdit() {
      this.isEditing = !this.isEditing;
    },
    
    getUserInfo(id,year,semester) {
      const path = `http://localhost:5000/tcs_StuAcc/${id}/${year}/${semester}`;
      axios.get(path)
        .then((res) => {
          this.user = res.data.acc_info[0];
          this.user.name = this.$route.params.name;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  }
};
</script>

<style scoped>
.user-info {
  max-width: 600px;
  margin: 0 auto;
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: left;
}

.user-info h2 {
  text-align: center;
  color: #333;
}

.user-info p,
.user-info input {
  font-size: 18px;
  line-height: 1.6;
  color: #555;
  margin: 10px 0;
}

.user-info p span {
  font-weight: bold;
  color: #333;
}

.user-info input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.user-info button {
  padding: 10px 20px;
  background-color: #2d68a894;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin: 10px 5px;
}

.user-info button:hover {
  background-color: #1a4e7a;
}
</style>