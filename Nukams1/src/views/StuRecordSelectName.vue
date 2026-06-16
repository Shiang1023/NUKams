<template>
  <div class="StuAccSel_main">
    <main>
      <div class="search-container">
        <input type="text" v-model="searchQuery" placeholder="搜尋學號或姓名...">
      </div>
      <div class="select-container">
        <select v-model="selectedGrade" @change="updateUrlParams">
          <option value="">請選擇學年</option>
          <option value="112">112</option>
          <option value="111">111</option>
          <option value="110">110</option>
          <option value="109">109</option>
        </select>
        <select v-model="selectedSemester" @change="updateUrlParams">
          <option value="">請選擇學期</option>
          <option value="1">第一學期</option>
          <option value="2">第二學期</option>
        </select>
      </div>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>學號</th>
              <th>姓名</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="student in filteredStudents" :key="student.student_id">
              <td v-if="selectedGrade && selectedSemester">
                <router-link
                  :to="{
                    name: 'StuRecord',
                    params: {
                      id: student.student_id,
                      name: student.name,
                      grade: selectedGrade,
                      semester: selectedSemester,
                      tid: this.$route.params.id
                    }
                  }"
                >{{ student.student_id }}</router-link>
              </td>
              <td v-else>{{ student.student_id }}</td>
              <td v-if="selectedGrade && selectedSemester">
                <router-link
                  :to="{
                    name: 'StuRecord',
                    params: {
                      id: student.student_id,
                      name: student.name,
                      grade: selectedGrade,
                      semester: selectedSemester,
                      tid: this.$route.params.id
                    }
                  }"
                >{{ student.name }}</router-link>
              </td>
              <td v-else>{{ student.name }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';

export default {
  name: 'StuRecordSelectName',
  data() {
    return {
      searchQuery: '',
      selectedGrade: '',
      selectedSemester: '',
      students: []
    };
  },
  computed: {
    filteredStudents() {
      return this.students.filter(student => {
        return student && student.student_id && student.name &&
          (student.student_id.includes(this.searchQuery) || student.name.includes(this.searchQuery));
      });
    }
  },
  methods: {
    getSelectName(id) {
      const path = `http://localhost:5000/SelectName/${id}`;
      axios.get(path)
        .then((res) => {
          this.students = res.data.names;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    updateUrlParams() {
      this.$router.push({ query: { grade: this.selectedGrade, semester: this.selectedSemester } });
    }
  },
  created() {
    this.getSelectName(this.$route.params.id);
  }
};
</script>

<style scoped>
/* CSS styles go here */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}
header {
  background-color: #2d68a894;
  padding: 10px;
  color: white;
}

main {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-direction: column;
    padding: 20px;
    text-align:center;
    max-height: 650px;
  }
  
  .table-container {
    width: 80%;
    max-height: 500px;
    overflow-y: auto;
    margin: 0 auto;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-bottom: 40px;
  }
  
  table {
    border-collapse: collapse;
    width: 100%;
  }
  
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
  }
  
  th {
    background-color: #2d68a894;
    color: white;
  }
  
  tr:nth-child(even) {
    background-color: #f2f2f2;
  }
  
  tr:hover {
    background-color: #ddd;
  }
  
  td a {
    color: #05070894;
    text-decoration: none;
  }
  
  td a:hover {
    text-decoration: underline;
  }
  
  .search-container {
    width: 80%;
    margin: 10px auto;
    text-align: center;
    display: flex;
    justify-content: center;
   margin-bottom: 30px;
  }
  
  .search-container input {
    padding: 10px;
    width: 80%;
    font-size: 1em;
    border: 1px solid #ddd;
    border-radius: 5px;
    outline: none;
  }
footer {
  background-color: #2d68a894;
  color: white;
  padding: 10px;
  text-align: center;
}

.select-container {
  width: 80%;
  margin: 10px auto;
  text-align: center;
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
}
.select-container select {
  padding: 10px;
  font-size: 1em;
  border: 1px solid #ddd;
  border-radius: 5px;
  outline: none;
  margin-right: 10px;
}
.StuAccSel_main{
  width: 100%;
  max-height: 550px; /* 限制最大高度 */
  overflow-y: auto; /* 添加垂直滚动条 */
}
</style>
