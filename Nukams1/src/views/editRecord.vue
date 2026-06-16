<template>
  <div id="app">
  

    
  <main style="padding-top: 10px;">
      <div class="form-section" v-if="!formSubmitted">
        <h3 class="title3">訪視紀錄表</h3>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="date">日期</label>
            <input type="date" id="date" v-model="form.date">
          </div>
          <div class="form-group">
            <label for="studentName">學生姓名</label>
            <input type="text" id="studentName" v-model="this.$route.params.name" disabled>
          </div>
          <div class="form-group">
            <label style="background-color: #e7e3e3; font-weight: bold;">環境與情況評估(導師填寫)</label>
            <br>
            <div class="radio-group">
              <label for="visitDetails" style="font-weight: bold;">押金要求</label>
              <div class="radio-options" style="margin-left: 25px;">
                <input type="radio" id="depositYes" value="合理" v-model="form.deposit">
                <label for="depositYes">合理</label>
                <input type="radio" id="depositNo" value="不合理" v-model="form.deposit">
                <label for="depositNo">不合理(2個月以上之租金)</label>
              </div>
            </div>
            <div class="radio-group">
              <label for="visitDetails" style="font-weight: bold;">水電費要求</label>
              <div class="radio-options">
                <input type="radio" id="billYes" value="合理" v-model="form.bill">
                <label for="billYes">合理</label>
                <input type="radio" id="billNo" value="不合理" v-model="form.bill">
                <label for="billNo">不合理</label>
              </div>
            </div>
            <div class="radio-group">
              <label for="visitDetails" style="font-weight: bold;">居家環境</label>
              <div class="radio-options">
                <input type="radio" id="environmentYes" value="佳" v-model="form.environment">
                <label for="environmentYes">佳</label>
                <input type="radio" id="environmentMid" value="適中" v-model="form.environment">
                <label for="environmentMid">適中</label>
                <input type="radio" id="environmentBad" value="欠佳" v-model="form.environment">
                <label for="environmentBad">欠佳，說明</label>
                <input type="text" id="environmentDetails" v-model="form.environmentDetails">
              </div>
            </div>
            <div class="radio-group">
              <label for="visitDetails" style="font-weight: bold;">生活設施</label>
              <div class="radio-options">
                <input type="radio" id="facilitiesYes" value="佳" v-model="form.facilities">
                <label for="facilitiesYes">佳</label>
                <input type="radio" id="facilitiesMid" value="適中" v-model="form.facilities">
                <label for="facilitiesMid">適中</label>
                <input type="radio" id="facilitiesBad" value="欠佳" v-model="form.facilities">
                <label for="facilitiesBad">欠佳，說明</label>
                <input type="text" id="facilitiesDetails" v-model="form.facilitiesDetails">
              </div>
            </div>
            <div class="radio-group">
              <label for="visitDetails" style="font-weight: bold;">訪視現況</label>
              <div class="radio-options">
                <input type="radio" id="visitStatus1" value="良好" v-model="form.visitStatus">
                <label for="visitStatus1">良好</label>
                <input type="radio" id="visitStatus2" value="適中" v-model="form.visitStatus">
                <label for="visitStatus2">適中</label>
                <input type="radio" id="visitStatus3" value="待加強" v-model="form.visitStatus">
                <label for="visitStatus3">待加強，說明</label>
                <input type="text" id="visitStatusDetails" v-model="form.visitStatusDetails">
              </div>
            </div>
            <div class="radio-group">
              <label for="visitDetails" style="font-weight: bold;">主客相處</label>
              <div class="radio-options" style="margin-left: 25px;">
                <input type="radio" id="well1" value="良好" v-model="form.well">
                <label for="well1">良好</label>
                <input type="radio" id="well2" value="待加強" v-model="form.well">
                <label for="well2">待加強</label>
              </div>
            </div>
            <label style="background-color: #e7e3e3; font-weight: bold;">訪視結果(導師填寫)</label>
            <br>
            <div class="radio-group">
              <div class="radio-options">
                <input type="radio" id="visitResult1" value="整體租賃狀況良好" v-model="form.visitResult">
                <label for="visitResult1">整體租賃狀況良好</label>
                <input type="radio" id="visitResult2" value="聯繫家長關注" v-model="form.visitResult">
                <label for="visitResult2">聯繫家長關注</label>
                <input type="radio" id="visitResult3" value="安全堪慮請協助" v-model="form.visitResult">
                <label for="visitResult3">安全堪慮請協助</label>
                <input type="radio" id="visitResult4" value="其他" v-model="form.visitResult">
                <label for="visitResult4">其他，說明:</label>
                <input type="text" id="visitResultDetails" v-model="form.visitResultDetails">
              </div>
            </div>
            <div class="input-label-wrapper">
              <label>其他記載或建議事項:</label>
              <input type="text" id="visitResultOthers" v-model="form.visitResultOthers">
            </div>
            <div class="form-group">
              <br>
              <br>
              <button type="submit" class="modify_button" style="margin-left: 20px; font-size: 20px;">確認送出</button>
            </div>
          </div>
        </form>
      </div>
      <div v-if="formSubmitted">
        <h3>填寫完畢</h3>
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
      formSubmitted: false,
    };
  },
  created() {
    this.getTeaRecordInfo(this.$route.params.id, this.$route.params.name, this.$route.params.tid);
  },
  methods: {
    updateTeaRecordInfo() {
      const path = `http://localhost:5000/get_TeaRecord/${this.$route.params.id}/112/2/${this.$route.params.tid}`;
      console.log("Updating user info with data: ", this.form); // 調試輸出
      axios.post(path, this.form)
        .then(response => {
          
        })
        .catch(error => {
          console.error(error);
        });
    },
    submitForm() {
       //檢查date是否在112學年第二學期
       if (this.form.date < '2024-02-21' || this.form.date > '2024-06-30') {
        alert('日期不在112學年第二學期範圍內！');
        return;
      } else if (
        !this.form.date ||
        !this.form.deposit ||
        !this.form.bill ||
        !this.form.environment ||
        (this.form.environment === '欠佳' && !this.form.environmentDetails) ||
        !this.form.facilities ||
        (this.form.facilities === '欠佳' && !this.form.facilitiesDetails) ||
        !this.form.visitStatus ||
        (this.form.visitStatus === '待加強' && !this.form.visitStatusDetails) ||
        !this.form.well ||
        !this.form.visitResult ||
        (this.form.visitResult === '其他' && !this.form.visitResultDetails)
      ) {
        alert('請確保所有選項都已填寫！');
        return;
      } else {
        alert('訪視紀錄已送出！');
        this.formSubmitted = true;
      }
     
      this.updateTeaRecordInfo();
    },
    getTeaRecordInfo(id,name,tid) {
      const path = `http://localhost:5000/get_TeaRecord/${id}/112/2/${tid}`;
      axios.get(path)
        .then((res) => {
          this.form = res.data.teaRecord_info[0];
          this.form.id = res.data.teaRecord_info[0].id; // 將 id 賦值給 this.user.id
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  watch: {
    'form.visitResult'(newValue) {
      if (newValue !== '其他') {
        this.form.visitResultDetails = ''; // Clear visitResultDetails field
      }
    },
    'form.environment'(newValue) {
      if (newValue !== '欠佳') {
        this.form.environmentDetails = ''; // Clear environmentDetails field
      }
    },
    'form.facilities'(newValue) {
      if (newValue !== '欠佳') {
        this.form.facilitiesDetails = ''; // Clear facilitiesDetails field
      }
    },
    'form.visitStatus'(newValue) {
      if (newValue !== '待加強') {
        this.form.visitStatusDetails = ''; // Clear visitStatusDetails field
      }
    }
  }
};
</script>
<style scoped>
body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    
    main {
      padding: 20px;
      max-width: 1500px;
      margin: 0 auto;
      max-height: 550px;/* 100%视窗高度减去页眉和页脚的高度 */
      overflow-y: auto; /* 当内容超出时显示滚动条 */
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
    .form-section {
      margin-bottom: 20px;
    }
    .form-section h3 {
      margin-bottom: 10px;
    }
    .form-group {
      margin-bottom: 10px;
    }
    .form-group label {
      display: block;
      margin-bottom: 5px;
      text-align: left;
    }
    .form-group input,
    .form-group select,
    .form-group textarea {
      width: 100%;
      padding: 8px;
      box-sizing: border-box;
    }
    .radio-group {
      display: flex;
      align-items: center;
      margin-bottom: 30px;
    }
    .radio-group label {
      margin-right: 30px;
      white-space: nowrap;
    }
    .radio-group input[type="text"] {
      flex: 1;
      margin-left: 10px;
    }
    .radio-options {
      display: flex;
      align-items: center;
      justify-content: flex-start;
      margin-left: 10px;
    }
    .radio-options label {
      margin-right: 10px;
    }
    #environmentDetails {
      width: 300px; 
    }
    #facilitiesDetails{
      width: 300px; 
    }
    #visitStatusDetails{
      width: 300px; 
    }
    #visitResultDetails{
        width: 300px; 
    }
    #visitResultOthers{
        width: 300px; 
    }
    .input-label-wrapper {
        display: flex;
        align-items: center;
    }
    .input-label-wrapper label {
        margin-left: 25px; /* Reset margin-left */
        margin-right: 10px; /* Add spacing between label and input */
        text-align: left; /* Align text to the left */
    }


    input[type="text"] {
      border: 1px solid #ccc; /* Add border style */
      border-radius: 4px; /* Optional: Add border radius for rounded corners */
    }
    input[type="date"] {
      border: 1px solid #ccc; /* Add border style */
      border-radius: 4px; /* Optional: Add border radius for rounded corners */
    }
    .title3 {
      font-weight: bold;
      text-align: center;
    }

    .modify_button {
      display: inline-block;
      font-size: 1.2em;
    
      padding: 10px 20px;
      color: #000;
      background-color: #f0f0f0;
      border: 1px solid #ccc;
      border-radius: 5px;
      cursor: pointer;
    }
    

    

</style>
