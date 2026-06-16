<template>
  <div id="app">
    <div class="content">
      <aside>
        <button @click="showList('租約')">租約</button>
        <button @click="showList('租戶')">租戶</button>
      </aside>
      <main>
        <div class="search-container" v-if="currentList">
          <input type="text" v-model="searchQuery" placeholder="搜尋租約或租戶...">
        </div>
        <div class="list-details-container">
          <div class="list" v-if="currentList === '租約'">
            <div class="list-header">
              <button @click="addItem">新增租約</button>
            </div>
            <div class="list-item" v-for="item in filteredListItems" :key="item.id" @click="showDetails(item)">
              {{ item.contract_id }}
            </div>
          </div>
          <div class="list" v-if="currentList === '租戶'">
            <div class="list-header">
              <!-- <button @click="addItem">新增租戶</button> -->
            </div>
            <div class="list-item" v-for="item in filteredListItems" :key="item.id" @click="showDetails(item)">
              {{ item.name }}
            </div>
          </div>
          <div class="details" v-if="selectedItem">
            <div v-if="!isEditing">
              <h2 v-if="currentList === '租約'">{{ selectedItem.contract_id }}</h2>
              <p v-if="currentList === '租約'"><strong>合約編號:</strong> {{ selectedItem.contract_id }}</p>
              <p v-if="currentList === '租約'"><strong>承租人:</strong> {{ selectedItem.name }}</p>
              <p v-if="currentList === '租約'"><strong>出租人:</strong> {{selectedItem.Landlord}}</p>
              <p v-if="currentList === '租約'"><strong>租賃期間:</strong> {{ selectedItem.RentTime }}</p>
              <p v-if="currentList === '租約'"><strong>租金(每月):</strong> {{ selectedItem.Rent }}</p>
              <p v-if="currentList === '租約'"><strong>押金:</strong> {{ selectedItem.deposit }}</p>
              <p v-if="currentList === '租約'"><strong>房屋地址:</strong> {{ selectedItem.address }}</p>
              
              <p v-if="currentList === '租戶'"><strong>姓名:</strong> {{ selectedItem.name }}</p>
              <p v-if="currentList === '租戶'"><strong>學號:</strong> {{ selectedItem.studentId }}</p>
              <p v-if="currentList === '租戶'"><strong>年級:</strong> {{ selectedItem.grade }}</p>
              <p v-if="currentList === '租戶'"><strong>導師:</strong> {{ selectedItem.advisor }}</p>
              <p v-if="currentList === '租戶'"><strong>性別:</strong> {{ selectedItem.gender }}</p>
              <p v-if="currentList === '租戶'"><strong>電子郵件:</strong> {{ selectedItem.email }}</p>
              <p v-if="currentList === '租戶'"><strong>電話號碼:</strong> {{ selectedItem.phone }}</p>
              <p v-if="currentList === '租戶'"><strong>家裡地址:</strong> {{ selectedItem.homeAddress }}</p>
              <p v-if="currentList === '租戶'"><strong>家裡電話:</strong> {{ selectedItem.homePhone }}</p>
              <p v-if="currentList === '租戶'"><strong>家裡聯絡人:</strong> {{ selectedItem.homeContact }}</p>
              <button v-if="currentList === '租約'" @click="toggleEdit">修改</button>
              <button v-if="currentList === '租約'" @click="deleteItem(selectedItem)">刪除</button>
            </div>
            <form v-else @submit.prevent="saveEdit">
              <label v-if="currentList === '租約'">合約編號</label>
              <input v-if="currentList === '租約'" type="text" v-model="selectedItem.contract_id" readonly>

              <label v-if="currentList === '租約'">承租人</label>
              <input v-if="currentList === '租約'" type="text" v-model="selectedItem.name" readonly>
        
              <label v-if="currentList === '租約'">出租人</label>
              <input v-if="currentList === '租約'" type="text" v-model="selectedItem.Landlord" readonly>
              
              <label v-if="currentList === '租約'">租賃期間</label>
              <input v-if="currentList === '租約'" type="text" v-model="selectedItem.RentTime" maxlength="20">
              
              <label v-if="currentList === '租約'">租金(每月)</label>
              <input v-if="currentList === '租約'" type="text" v-model="selectedItem.Rent" maxlength="10">
              
              <label v-if="currentList === '租約'">押金</label>
              <input v-if="currentList === '租約'" type="text" v-model="selectedItem.deposit" maxlength="15">

              <label v-if="currentList === '租約'">房屋地址</label>
              <input v-if="currentList === '租約'" type="text" v-model="selectedItem.address" maxlength="30">
              
              <label v-if="currentList === '租戶'">姓名</label>
              <input v-if="currentList === '租戶'" type="text" v-model="selectedItem.name">
              
              <label v-if="currentList === '租戶'">學號</label>
              <input v-if="currentList === '租戶'" type="text" v-model="selectedItem.studentId">
              
              <label v-if="currentList === '租戶'">年級</label>
              <input v-if="currentList === '租戶'" type="text" v-model="selectedItem.grade">
              
              <label v-if="currentList === '租戶'">導師</label>
              <input v-if="currentList === '租戶'" type="text" v-model="selectedItem.advisor">
              
              <label v-if="currentList === '租戶'">性別</label>
              <input v-if="currentList === '租戶'" type="text" v-model="selectedItem.gender">
              
              <label v-if="currentList === '租戶'">電子郵件</label>
              <input v-if="currentList === '租戶'" type="text" v-model="selectedItem.email">
              
              <label v-if="currentList === '租戶'">電話號碼</label>
              <input v-if="currentList === '租戶'" type="text" v-model="selectedItem.phone">
              
              <label v-if="currentList === '租戶'">家裡地址</label>
              <input v-if="currentList === '租戶'" type="text" v-model="selectedItem.homeAddress">
              
              <label v-if="currentList === '租戶'">家裡電話</label>
              <input v-if="currentList === '租戶'" type="text" v-model="selectedItem.homePhone">
              
              <label v-if="currentList === '租戶'">家裡聯絡人</label>
              <input v-if="currentList === '租戶'" type="text" v-model="selectedItem.homeContact">

              <button type="submit">完成</button>
              <button @click="toggleEdit">取消</button>
            </form>
          </div>
          <div class="newcontract" v-if="isAdding">
            <form @submit.prevent="saveNewItem(this.$route.params.id)">
              
              
              <label v-if="currentList === '租約'">學號</label>
              <input v-if="currentList === '租約'" type="text" v-model="newItem.studentId" required maxlength="10">
              
              <label v-if="currentList === '租約'">租賃期間</label>
              <input v-if="currentList === '租約'" type="text" v-model="newItem.RentTime" required maxlength="20">
              
              <label v-if="currentList === '租約'">租金(每月)</label>
              <input v-if="currentList === '租約'" type="text" v-model="newItem.Rent" required maxlength="10">
              
              <label v-if="currentList === '租約'">押金</label>
              <input v-if="currentList === '租約'" type="text" v-model="newItem.deposit" required maxlength="15">
              
              <label v-if="currentList === '租約'">房屋地址</label>
              <input v-if="currentList === '租約'" type="text" v-model="newItem.address" required maxlength="30">

              <button type="submit">完成</button>
              <button @click="isAdding = false">取消</button>
            </form>
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
      searchQuery: '',
      isAdding: false,
      isEditing: false,
      newItem: {
        studentId: '',
        RentTime: '',
        RentTime: '',
        Rent: '',
        deposit: '',
        address: '',
      },
      selectedItem: null,
      items: [] ,
      leaseList: [
        
      ],
      renterList: [
        
      ]
    };
  },
  // created() {
  //   this.getUserInfo(this.$route.params.id);
  //   console.log(this.$route.params.id);
  // },
  computed: {
    filteredListItems() {
      let list = this.currentList === '租約' ? this.leaseList : this.renterList;
      return list.filter(item => {
        if (this.currentList === '租約') {
          return item.contract_id.includes(this.searchQuery);
        } else {
          return item.name.includes(this.searchQuery);
        }
      });
    }
  },
  methods: {
    getUserInfo(id) {
      const path = `http://127.0.0.1:5000/api/landlord/renter_information/${id}`;
      console.log(path);
      axios.get(path)
        .then((res) => {
          const data = res.data.renter_information;
          this.leaseList = data.map(item => ({
            contract_id: item.contract_id,
            name: item.name,
            Landlord: item.Landlord,
            RentTime: item.RentTime,
            Rent: item.Rent,
            deposit: item.deposit,
            address: item.address
          }));
          this.renterList = data.map(item => ({
            name: item.name,
            idNumber: item.idNumber,
            studentId: item.studentId,
            grade: item.grade,
            advisor: item.advisor,
            gender: item.gender,
            email: item.email,
            phone: item.phone,
            homeAddress: item.homeAddress,
            homePhone: item.homePhone,
            homeContact: item.homeContact
          }));
          console.log(this.leaseList, this.renterList);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    showList(listType) {
      this.getUserInfo(this.$route.params.id);
      this.currentList = listType;
      this.selectedItem = null;
      this.isAdding = false;
      this.isEditing = false;
      this.searchQuery = '';
    },

    showDetails(item) {
      this.selectedItem = item;
      this.isAdding = false;
      this.isEditing = false;
    },
    addItem() {
      this.isAdding = true;
      this.selectedItem = null;
      this.isEditing = false;
      this.newItem = {
        contract_id: '',
        name: '',
        Landlord: '',
        RentTime: '',
        Rent: '',
        deposit: '',
        address: '',
        studentId: '',
        grade: '',
        advisor: '',
        gender: '',
        email: '',
        phone: '',
        homeAddress: '',
        homePhone: '',
        homeContact: ''
      };
    },
    async saveNewItem(id) {
      try {
        console.log("IIIDDD",id);
        const response = await axios.get(`http://127.0.0.1:5000/api/landlord/add_new_contract/${id},${this.newItem.studentId},${this.newItem.RentTime},${this.newItem.deposit},${this.newItem.address},${this.newItem.Rent}`);
        console.log(this.newItem)
        console.log(response);
        if (response.status === 200) {
          const data = response.data;
          console.log("123");
          this.items.push(data); // Add the new item to the items array
          this.isAdding = false;
          this.newItem = {
            contract_id: '',
            name: '',
            Landlord: '',
            RentTime: '',
            Rent: '',
            deposit: '',
            address: '',
          };
          window.location.reload();
        } else {
          console.error('Failed to save the item');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
    toggleEdit() {
      this.isEditing = !this.isEditing;
    },
    saveEdit() {
      const path = `http://127.0.0.1:5000/api/landlord/update_contract/${this.selectedItem.contract_id},${this.selectedItem.RentTime},${this.selectedItem.deposit},${this.selectedItem.address},${this.selectedItem.Rent}`;
      console.log("Updating user info with data: ", this.selectedItem);
      axios.get(path, this.leaseList)
        .then(response => {
          console.log(response);
          this.isEditing = false;
        })
        .catch(error => {
          console.error(error);
        });
      this.isEditing = false;
    },
    deleteItem(item) {
      console.log("ID",item.contract_id);
      const path = `http://127.0.0.1:5000/api/landlord/delete_contract/${item.contract_id}`;
      axios.get(path, { id: item.contract_id })
        .then(response => {
          console.log(response);
          if (this.currentList === '租約') {
        const index = this.leaseList.findIndex(i => i.id === item.id);
        if (index !== -1) {
          this.leaseList.splice(index, 1);
          const renterIndex = this.renterList.findIndex(r => r.name === item.name);
          if (renterIndex !== -1) {
            this.renterList.splice(renterIndex, 1);
          }
          this.selectedItem = null;
        }
      } else if (this.currentList === '租戶') {
        const index = this.renterList.findIndex(i => i.id === item.id);
        if (index !== -1) {
          this.renterList.splice(index, 1);
          this.selectedItem = null;
        }
      }
        })
        .catch(error => {
          console.error(error);
        });

    },
    cancelAdd() {
      this.isAdding = false;
    },
    navigateTo(path) {
      this.$router.push(path);
    }
  }
};
</script>

<style scoped>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f5f5f5;
  color: #333;
  height: 100vh;
  display: flex;
  flex-direction: column;
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
  justify-content: space-between;
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
  overflow: hidden; 
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
  height: 100%; 
  overflow: auto; 
}
.list {
  width: 100%;
  max-width: 600px;
}
.list-item {
  padding: 10px;
  border-bottom: 1px solid #ccc;
  cursor: pointer;
}
.list-item:hover {
  background-color: #eee;
}
.list-details-container {
  display: flex;
  width: 100%;
  max-width: 1200px;
}
.list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
.list-header button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}
.list-header button:hover {
  background-color: #45a049;
}
.newcontract {
  width: 50%;
  max-width: 600px;
  margin: 0 20px;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.newcontract p, .newcontract input, .newcontract label {
  font-size: 18px;
  line-height: 1.6;
  color: #555;
  margin: 10px 0;
}
.newcontract input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.newcontract button {
  padding: 10px 20px;
  background-color: #2d68a894;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin: 10px 5px;
}
.newcontract button:hover {
  background-color: #1a4e7a;
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
.details p, .details input, .details label {
  font-size: 18px;
  line-height: 1.6;
  color: #555;
  margin: 10px 0;
}
.details input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.details button {
  padding: 10px 20px;
  background-color: #2d68a894;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin: 10px 5px;
}
.details button:hover {
  background-color: #1a4e7a;
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
.error {
  color: red;
  margin: 10px 0;
}
footer {
  background-color: #2d68a894;
  color: #fff;
  padding: 10px;
  text-align: center;
  width: 100%;
}
</style>