<template>
    <div id="app">
      
      <main>

        <div class="form-section" v-if="!formSubmitted">
          <h3>訪視紀錄表</h3>
          <br>
          <form @submit.prevent="updateStRecordInfo">

            <div class="input-label-wrapper">
                <label>學號:</label>
                <input type="text" id="studentId" v-model="form.id":disabled=true required>
              </div>
              <br>
            
            <div class="form-group">
              <label style="background-color: #e7e3e3; font-weight: bold;">校外居住狀況(學生填寫)</label>
              <br>
              <div class="input-label-wrapper">
                <label>連絡電話:</label>
                <input type="text" id="phone" v-model="form.phone":disabled="!isEditing" required>
              </div>
              <br>
              <div class="input-label-wrapper">
                <label>房東姓名:</label>
                <input type="text" id="landlordName" v-model="form.landlordName":disabled="!isEditing" required>
              </div>
              <br>
              <div class="input-label-wrapper">
                <label>房東電話:</label>
                <input type="text" id="landlordPhone" v-model="form.landlordPhone":disabled="!isEditing" required>
              </div>
              <br>
              <div class="input-label-wrapper">
                <label>居住地址:</label>
                <input type="text" id="studentAddress" v-model="form.studentAddress":disabled="!isEditing" required>
              </div>
              <br>
              <div class="input-label-wrapper">
                <label>每月租金:</label>
                <input type="text" id="monthlyRent" v-model="form.monthlyRent":disabled="!isEditing" required>
              </div>
              <br>
              <div class="input-label-wrapper">
                <label>押金:</label>
                <input type="text" id="deposit" v-model="form.deposit":disabled="!isEditing" required>
              </div>
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">租屋型態</label>
                <div class="radio-options">
                  <input type="radio" id="house" value="獨棟透天" v-model="form.houseType":disabled="!isEditing" required>
                  <label for="house">獨棟透天</label>
                  <input type="radio" id="departmentFive" value="大樓公寓(五層樓以下)" v-model="form.houseType":disabled="!isEditing" required>
                  <label for="departmentFive">大樓公寓(五層樓以下)</label>
                  <input type="radio" id="departmentSix" value="大樓公寓(六層樓以上)" v-model="form.houseType":disabled="!isEditing" required>
                  <label for="departmentSix">大樓公寓(六層樓以上)</label>
                  <input type="radio" id="collegeDorm" value="大學宿舍" v-model="form.houseType":disabled="!isEditing" required>
                  <label for="collegeDorm">大學宿舍</label>
                </div>
              </div>
            </div>
            <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">房間類型</label>
                <div class="radio-options">
                  <input type="radio" id="noBathroom" value="雅房" v-model="form.roomType":disabled="!isEditing" required>
                  <label for="noBathroom">雅房</label>
                  <input type="radio" id="yesBathroom" value="套房" v-model="form.roomType":disabled="!isEditing" required>
                  <label for="yesBathroom">套房</label>
                </div>
              </div>
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">是否推薦其他同學租住</label>
                <div class="radio-options">
                  <input type="radio" id="Recommend" value="推薦" v-model="form.recommend":disabled="!isEditing" required>
                  <label for="Recommend">推薦</label>
                  <input type="radio" id="notRecommend" value="不推薦" v-model="form.recommend":disabled="!isEditing" required>
                  <label for="notRecommend">不推薦</label>
                </div>
              </div>
            
            <div class="form-group">
              <label style="background-color: #e7e3e3; font-weight: bold;">居住安全自主檢視資料(學生填寫)</label>
              <br>
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">木造隔間及鐵皮加蓋</label>
                <div class="radio-options">
                  <input type="radio" id="woodYes" value="是" v-model="form.woodStructure":disabled="!isEditing" required>
                  <label for="woodYes">是</label>
                  <input type="radio" id="woodNo" value="否" v-model="form.woodStructure":disabled="!isEditing" required>
                  <label for="woodNo">否</label>
                </div>
              </div>
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">有火警警報器或偵煙器</label>
                <div class="radio-options">
                  <input type="radio" id="fireYes" value="是" v-model="form.fireAlarm":disabled="!isEditing" required>
                  <label for="fireYes">是</label>
                  <input type="radio" id="fireNo" value="否" v-model="form.fireAlarm":disabled="!isEditing" required>
                  <label for="fireNo">否</label>
                </div>
              </div>
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">逃生通道暢通且標示清楚</label>
                <div class="radio-options">
                  <input type="radio" id="hallwayYes" value="是" v-model="form.escapeRoute":disabled="!isEditing" required>
                  <label for="hallwayYes">是</label>
                  <input type="radio" id="hallwayNo" value="否" v-model="form.escapeRoute":disabled="!isEditing" required>
                  <label for="hallwayNo">否</label>
                </div>
              </div>
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">門鎖及鎖具是否管理良好</label>
                <div class="radio-options">
                  <input type="radio" id="lockYes" value="是" v-model="form.lockManagement":disabled="!isEditing" required>
                  <label for="lockYes">是</label>
                  <input type="radio" id="lockNo" value="否" v-model="form.lockManagement":disabled="!isEditing" required>
                  <label for="lockNo">否</label>
                </div>
              </div>
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">有安裝照明設備</label>
                <div class="radio-options">
                  <input type="radio" id="lightYes" value="是" v-model="form.lighting":disabled="!isEditing" required>
                  <label for="lightYes">是</label>
                  <input type="radio" id="lightNo" value="否" v-model="form.lighting":disabled="!isEditing" required>
                  <label for="lightNo">否</label>
                </div>
              </div>
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">了解及熟悉電路安全及逃生要領</label>
                <div class="radio-options">
                  <input type="radio" id="electricYes" value="是" v-model="form.circuitSafety":disabled="!isEditing" required>
                  <label for="electricYes">是</label>
                  <input type="radio" id="electricNo" value="否" v-model="form.circuitSafety":disabled="!isEditing" required>
                  <label for="electricNo">否</label>
                </div>
              </div>
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">了解派出所及消防隊等專線電話</label>
                <div class="radio-options">
                  <input type="radio" id="policeYes" value="是" v-model="form.emergencyContacts":disabled="!isEditing" required>
                  <label for="policeYes">是</label>
                  <input type="radio" id="policeNo" value="否" v-model="form.emergencyContacts":disabled="!isEditing" required>
                  <label for="policeNo">否</label>
                </div>
              </div>
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">使用多種電器是否插在同一條延長線</label>
                <div class="radio-options">
                  <input type="radio" id="electricEquipmentYes" value="是" v-model="form.electricEquipment":disabled="!isEditing" required>
                  <label for="electricEquipmentYes">是</label>
                  <input type="radio" id="electricEquipmentNo" value="否" v-model="form.electricEquipment":disabled="!isEditing" required>
                  <label for="electricEquipmentNo">否</label>
                </div>
              </div>
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">有滅火器且功能正常</label>
                <div class="radio-options">
                  <input type="radio" id="hydrantYes" value="是" v-model="form.fireExtinguisher":disabled="!isEditing" required>
                  <label for="hydrantYes">是</label>
                  <input type="radio" id="hydrantNo" value="否" v-model="form.fireExtinguisher":disabled="!isEditing" required>
                  <label for="hydrantNo">否</label>
                </div>
              </div>
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">熱水器安全良好</label>
              
                <div class="radio-options">
                  <input type="radio" id="hotWaterYes" value="是" v-model="form.hotwater":disabled="!isEditing" required>
                  <label for="hotWaterYes">是</label>
                  <input type="radio" id="hotWaterNo" value="否" v-model="form.hotwater":disabled="!isEditing" required>
                  <label for="hotWaterNo">否</label>
                </div>
              </div>
      
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">分六個房間以上或十個床位以上</label>
              
                <div class="radio-options">
                  <input type="radio" id="roomBedYes" value="是" v-model="form.roombed":disabled="!isEditing" required>
                  <label for="roomBedYes">是</label>
                  <input type="radio" id="roomBedNo" value="否" v-model="form.roombed":disabled="!isEditing" required>
                  <label for="roomBedNo">否</label>
                </div>
              </div>
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">有安裝監視器</label>
              
                <div class="radio-options">
                  <input type="radio" id="CCTVYes" value="是" v-model="form.CCTVyes":disabled="!isEditing" required>
                  <label for="CCTVYes">是</label>
                  <input type="radio" id="CCTVNo" value="否" v-model="form.CCTVyes":disabled="!isEditing" required>
                  <label for="CCTVNo">否</label>
                </div>
              </div>
              <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">符合內政部政策</label>
              
                <div class="radio-options">
                  <input type="radio" id="lawYes" value="是" v-model="form.law":disabled="!isEditing" required>
                  <label for="lawYes">是</label>
                  <input type="radio" id="lawNo" value="否" v-model="form.law":disabled="!isEditing" required>
                  <label for="lawNo">否</label>
                </div>
              </div>
              
            </div>
            <div class="form-group">
              <button type="button" @click="toggleEdit" v-if="!isEditing">修改</button>
              <button type="submit" v-if="isEditing">完成</button>
            </div>
          </form>
        </div>
        <div class="submitted-message" v-else>
          <p>表單已成功提交！</p>
          <button @click="resetForm">重新填寫</button>
        </div>
      </main>
      
    </div>
  </template>
  
  <script setup>
import axios from 'axios';
import { ref } from 'vue';
</script>
<script>
export default {
  data() {
    return {
      form: {},
      isEditing: false,
    };
  },
  created() {
    this.getStRecordInfo(this.$route.params.id);
  },
  methods: {
    updateStRecordInfo() {
      const path = `http://localhost:5000/get_StRecord/${this.$route.params.id}`;
      console.log("Updating user info with data: ", this.form); // 調試輸出
      axios.post(path, this.form)
        .then(response => {
          this.getStRecordInfo(this.form.id); // 重新獲取用戶資訊
          this.form.id = this.$route.params.id;
          this.toggleEdit(); // 切換回非編輯模式
        })
        .catch(error => {
          this.form.id = this.$route.params.id;
          console.error(error);
        });
    },
  
    getStRecordInfo(id) {
      const path = `http://localhost:5000/get_StRecord/${id}`;
      axios.get(path)
        .then((res) => {
          this.form = res.data.stRecord_info[0];
         // this.form.id = res.data.stRecord_info[0].id; // 將 id 賦值給 this.user.id
         this.form.id = this.$route.params.id;
        })
        .catch((error) => {
          this.form.id = this.$route.params.id;
          console.error(error);
        });
    },
    toggleEdit() {
    this.isEditing = !this.isEditing;
  }
  }
};
</script>
  
  <style scoped>
  #app {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
  }
    
    header {
    background-color: #2d68a894;
    color: #fff;
    padding: 20px;
    text-align: center;
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
  .dropdown {
    position: relative;
    display: inline-block;
  }
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
  }
  .dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
  }
  .dropdown-content a:hover {
    background-color: #f1f1f1;
  }
  .dropdown:hover .dropdown-content {
    display: block;
  }
  main {
    padding: 1em;
  }
  .form-section {
    background-color: #f2f2f2;
    padding: 20px;
    border-radius: 8px;
    max-height: 530px; 
    overflow-y: auto; 
  }
  .form-section h3 {
    display: block;
    margin-bottom: 5px;
    color: rgb(12, 11, 11);
    background-color: #f2f2f20c;
  }
  .form-group {
    margin-bottom: 15px;
  }
  .form-group label {
    display: block;
    margin-bottom: 5px;
  }
  .form-group input,
  .form-group textarea {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  .form-group button {
    padding: 10px 20px;
    background-color: #2d68a8;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  .radio-group {
    margin-bottom: 15px;
  }
  .radio-options {
      display: flex;
      align-items: center;
      justify-content: flex-start;
      margin-left: 10px;
    }
    .radio-options label {
      margin-right: 30px;
      white-space: nowrap;
    }
  .submitted-message {
    text-align: center;
    padding: 20px;
    background-color: #e7f4e4;
    border: 1px solid #d4e8d0;
    border-radius: 8px;
  }
  footer {
      background-color: #2d68a894;
      color: #fff;
      padding: 10px;
      text-align: center;
      position: absolute;
      bottom: 0;
      width: 100%;
    }
  </style>
  



  <!-- 連絡電話、房東姓名、電話，地址、每月租金、押金、租屋型態、房間類型，推薦、木造 -->