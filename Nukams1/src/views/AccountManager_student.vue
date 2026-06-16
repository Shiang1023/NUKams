<template>
  <div class="wrapper">
    <nav>
      <aside>
        <router-link to="AccountManager_student">學生</router-link>
        <router-link to="AccountManager_teacher">老師</router-link>
        <router-link to="AccountManager_landlord">房東</router-link>
      </aside>
    </nav>
    <main>
      <div v-for="student in students" :key="student.id" class="button-container">
        <router-link :to="{ name: 'personalINFO_student', params: { id: student.id } }" class="button">
          <div class="student-info">
            <span>{{ student.id }} {{ student.name }}</span>
          </div>
        </router-link>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AccountManager_student',
  data() {
    return {
      students: [],
    };
  },
  created() {
    this.getStudents();
  },
  methods: {
    getStudents() {
      const path = 'http://127.0.0.1:5000/api/administrator/get_idandnames/3'; // Assuming this endpoint fetches student data
      axios.get(path)
        .then((res) => {
          this.students = res.data.all_idandnames_info;
        })
        .catch((error) => {
          console.error(error);
        });
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
  margin-left: 140px;
  flex-grow: 1;
  padding: 20px;
}

.button-container {
  text-align: center;
  margin-bottom: 10px;
}

.button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 600px;
  background-color: #2d68a894;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
  transition: background-color 0.3s;
  text-align: center;
}

.button:hover {
  background-color: #1e4b7e;
}

.student-info {
  display: flex;
  justify-content: center;
  width: 100%;
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
