<template>
  <div class="StuPerSele_main">
    <main>
      <div class="search-container">
        <input type="text" v-model="searchQuery" placeholder="搜尋學號或姓名...">
      </div>
      <div class="table-container">
        <table v-if="Object.keys(students).length > 0">
          <thead>
            <tr>
              <th>學號</th>
              <th>姓名</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="student in filteredStudents" :key="student.id">
              <td><router-link :to="{ name: 'editRecord', params: { id: student.student_id, name: student.name,tid:this.$route.params.id }}">{{ student.student_id }}</router-link></td>
              <td><router-link :to="{ name: 'editRecord', params: { id: student.student_id, name: student.name ,tid:this.$route.params.id}}">{{ student.name }}</router-link></td>
            </tr>
          </tbody>
        </table>
        <div v-else-if="showErrorMessage">
          抱歉,無法獲取學生資料。
        </div>
        <div v-else>
          <div class="loading-indicator">載入中...</div>
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
  name: 'editRecordSelectName',
  data() {
    return {
      searchQuery: '',
      students: {},
    };
  },
  created() {
    this.getSelectName(this.$route.params.id);
  },
  computed: {
    filteredStudents() {
      if (!Array.isArray(this.students) || this.students.length === 0) {
        return [];
      }
      return this.students.filter(student => student !== undefined && student.name.includes(this.searchQuery));
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
  },
};

</script>

  <style scoped>
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
    width: 40%;
    font-size: 1em;
    border: 1px solid #ddd;
    border-radius: 5px;
    outline: none;
  }
  .StuPerSele_main{
    width: 100%;
    max-height: 550px; /* 限制最大高度 */
    overflow-y: auto; /* 添加垂直滚动条 */
  }
 
  </style>