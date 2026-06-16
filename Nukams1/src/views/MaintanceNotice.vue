<template>
    <div id="app">
    
      <div class="content">
        <aside>
          <button @click="showList('修繕通知')">修繕通知</button>
          <button @click="showList('修繕計畫')">修繕計畫</button>
          
        </aside>
        <main>
          <div class="search-container" v-if="currentList">
            <input type="text" v-model="searchQuery" placeholder="搜尋修繕通知或修繕計畫...">
          </div>
          <div class="list-details-container">
            <div class="list" v-if="currentList">
              <div class="list-item" v-for="item in filteredListItems" :key="item.id" @click="showDetails(item)">
                <span>{{ item.name }}</span>
                <div>
                  <button class="action-button" v-if="currentList === '修繕通知'" @click="deleteItem('修繕通知', item.id)">刪除</button>
                  <button class="action-button" v-if="currentList === '修繕通知'" @click="addToPlan(item)">新增到修繕計畫</button>
                  <button class="action-button" v-if="currentList === '修繕計畫'" @click="deleteItem('修繕計畫', item.id)">刪除</button>
                </div>
              </div>
            </div>
            <div class="details" v-if="selectedItem">
              <h2>{{ selectedItem.name }}</h2>
              <p><strong>ID:</strong> {{ selectedItem.id }}</p>
              <p><strong>回報人:</strong> {{ selectedItem.reporter  }}</p>
              <p><strong>描述:</strong> {{ selectedItem.description }}</p>
              
            </div>
          </div>
        </main>
      </div>
      
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    data() {
    return {
      currentList: null,
      selectedItem: null,
      searchQuery: '',
      lists: {
        修繕通知: [
          { id: 1, name: '修繕通知 1', description: '修繕通知 1 的描述', reporter: '報告人 1' },
          { id: 2, name: '修繕通知 2', description: '修繕通知 2 的描述', reporter: '報告人 2' },
        ],
        修繕計畫: []
      }
    };
  },
  created() {
    // this.getrepairreportInfo(this.$route.params.id);
    console.log(this.$route.params.id);
  },
    methods: {
      getrepairreportInfo(id) {
    const path = `http://127.0.0.1:5000/api/landlord/return_response_equal_0/${id}`;
    axios.get(path)
      .then((res) => {
          const lists = res.data.repair_response_0.map(item => {
            return {
              id: item.id,
              name: item.description, // 假设 'description' 用于 'name'
              description: item.description,
              reporter: item.reporter
            };
          });

          // 更新 'lists' 对象以包含这些修繕通知
          this.lists.修繕通知 = lists;

          console.log(this.lists); // 验证更新后的 'lists' 对象
        
      })
      .catch((error) => {
        console.error(error);
      });
  },
      getreportplan(id) {
    const path = `http://127.0.0.1:5000/api/landlord/return_response_equal_1/${id}`;
    axios.get(path)
      .then((res) => {
        // Assuming res.data.repair_response_1 is an array of repair notices
        const lists = res.data.repair_response_1.map(item => {
          return {
            id: item.id,
            name: item.description, // Assuming 'description' is used for 'name'
            description: item.description,
            reporter: item.reporter
          };
        });

        // Update your 'lists' object to include these repair notices
        this.lists.修繕計畫 = lists;

        console.log(this.lists); // Verify the updated 'lists' object
      })
      .catch((error) => {
        console.error(error);
      });
  },
      navigateTo(route) {
        this.$router.push(route);
      },
      showList(listName) {
        if (listName === '修繕通知') {
          this.getrepairreportInfo(this.$route.params.id);
        } else if (listName === '修繕計畫') {
          this.getreportplan(this.$route.params.id);
        }
        
        this.currentList = listName;
        this.selectedItem = null;
        this.searchQuery = '';
      },
      showDetails(item) {
        this.selectedItem = item;
      },
      deleteItem(listName, itemId) {
        console.log('Deleting item:', itemId);
        const path = `http://127.0.0.1:5000/api/landlord/delete_repair/${itemId}`;
        axios.get(path, { id: itemId})
          .then(response => {
            this.lists[listName] = this.lists[listName].filter(item => item.id !== itemId);
            if (this.selectedItem && this.selectedItem.id === itemId) {
              this.selectedItem = null;
            }
          })
          .catch(error => {
            console.error(error);
          });
      },
      deletefromNotice(listName, itemId) {
        console.log('Deleting item:', itemId);
        this.lists[listName] = this.lists[listName].filter(item => item.id !== itemId);
        if (this.selectedItem && this.selectedItem.id === itemId) {
          this.selectedItem = null;
        }
      },
      addToPlan(item) {
        console.log('Adding item to plan:', item.id);
        const path = `http://127.0.0.1:5000/api/landlord/response_to_repair/${item.id}`;
        axios.get(path, { id: item.id })
          .then(response => {
            this.lists.修繕計畫.push(item);
            this.deletefromNotice('修繕通知', item.id);
          })
          .catch(error => {
            console.error(error);
          });
        
        
      }
    },
    computed: {
      currentListItems() {
        return this.currentList ? this.lists[this.currentList] : [];
      },
      filteredListItems() {
        return this.currentListItems.filter(item =>
          item.name.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }
    }
  };
  </script>
    
    <style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        flex-direction: column;
        min-height: 100vh;
      }
      nav {
        background-color: #f1f1f1;
        padding: 10px;
        text-align: center;
      }
      nav a {
        color: #333;
        text-decoration: none;
        padding: 10px;
        margin: 5px;
      }
      nav a:hover {
        background-color: #ddd;
      }
      #app {
        display: flex;
        flex-direction: column;
        flex: 1;
      }
      header {
        background-color: #2d68a894;
        color: #fff;
        padding: 20px;
        text-align: center;
      }
      .content {
        display: flex;
        flex: 1;
      }
      aside {
        background-color: #f1f1f1;
        width: 200px;
        padding: 10px;
        box-shadow: 2px 0 5px rgba(0,0,0,0.1);
      }
      aside button {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        background-color: #2d68a894;
        color: white;
        font-size: 16px;
      }
      aside button:hover {
        background-color: #1a4e7a;
      }
      main {
        padding: 20px;
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
      }
      .list-details-container {
          display: flex;
          width: 100%;
          max-width: 1200px;
        }
      .list {
        width: 100%;
        max-width: 600px;
      }
      .list-item {
        padding: 10px;
        border-bottom: 1px solid #ccc;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      .list-item:hover {
        background-color: #eee;
      }
      .details {
        width: 50%;
        max-width: 600px;
        margin: 0 20px;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      }
      .details p {
        font-size: 18px;
        line-height: 1.6;
        color: #555;
        margin: 10px 0;
      }
      .search-container {
        width: 100%;
        max-width: 600px;
        margin-bottom: 20px;
      }
      .search-container input {
        width: 100%;
        padding: 10px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 5px;
      }
      footer {
        background-color: #2d68a894;
        color: #fff;
        padding: 10px;
        text-align: center;
        width: 100%;
      }
      .action-button {
        padding: 5px 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        background-color: #2d68a894;
        color: white;
        font-size: 14px;
        margin-left: 10px;
      }
      .action-button:hover {
        background-color: #1a4e7a;
      }
    </style>
    