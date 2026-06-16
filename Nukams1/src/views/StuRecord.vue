<template>
  <div id="app">
    
  <main style="padding-top: 10px;">
    <div class="form-section" v-if="!formSubmitted">
        <h3 class="title3">訪視紀錄表</h3>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="date">日期</label>
            <input type="date" id="date" v-model="form2.date" disabled>
          </div>
          
          <div class="form-group">
            <label for="studentName">學生姓名</label>
            <input type="text" id="studentName" v-model="form.studentName" disabled>
          </div>
          <div class="form-group">
                <label for="teacherPhone">連絡電話</label>
                <input type="text" id="teacherPhone" v-model="form.teacherPhone" disabled>
          </div>
          <div class="form-group">
              <label style="background-color: #e7e3e3; font-weight: bold;">校外居住狀況(學生填寫)</label>
              <br>
              <div class="input-label-wrapper_s">
                <label>房東姓名:</label>
                <input type="text" id="landlordName" v-model="form.landlordName" disabled>
              </div>
              <br>
              <div class="input-label-wrapper_s">
                <label>房東電話:</label>
                <input type="text" id="landlordPhone" v-model="form.landlordPhone" disabled>
              </div>
              <br>
              <div class="input-label-wrapper_s">
                <label>居住地址:</label>
                <input type="text" id="studentAddress" v-model="form.studentAddress" disabled>
              </div>
              <br>
              <div class="input-label-wrapper_s">
                <label>每月租金:</label>
                <input type="text" id="monthlyRent" v-model="form.monthlyRent" disabled>
              </div>
              <br>
              <div class="input-label-wrapper_s">
                <label>押金:</label>
                <input type="text" id="deposit_s" v-model="form.deposit_s" disabled>
                <br><br>
              </div>

              </div>
              <div class="form-group_s">
            <div class="radio-group">
                <label for="visitDetails" style="font-weight: bold;">租屋型態</label>
            <div class="radio-options">
                <input type="radio" id="house" value="獨棟透天" v-model="form.houseType" :checked="form.houseType === '獨棟透天'" disabled>
                <label for="house">獨棟透天</label>
                <input type="radio" id="departmentFive" value="大樓公寓(五層樓以下)" v-model="form.houseType" :checked="form.houseType === '大樓公寓(五層樓以下)'" disabled>
                <label for="departmentFive">大樓公寓(五層樓以下)</label>
                <input type="radio" id="departmentSix" value="大樓公寓(六層樓以上)" v-model="form.houseType" :checked="form.houseType === '大樓公寓(六層樓以上)'" disabled>
                <label for="departmentSix">大樓公寓(六層樓以上)</label>
                <input type="radio" id="collegeDorm" value="大學宿舍" v-model="form.houseType" :checked="form.houseType === '大學宿舍'" disabled>
                <label for="collegeDorm">大學宿舍</label>
            </div>
        </div>
        <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">房間類型</label>
                <div class="radio-options_s">
                  <input type="radio" id="noBathroom" value="雅房" v-model="form.roomType" :checked="form.roomType==='雅房'" disabled>
                  <label for="noBathroom">雅房</label>
                  <input type="radio" id="yesBathroom" value="套房" v-model="form.roomType" :checked="form.roomType==='套房'" disabled>
                  <label for="yesBathroom">套房</label>
                </div>
              </div>
              <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">是否推薦其他同學租住</label>
                <div class="radio-options_s">
                  <input type="radio" id="Recommend" value="推薦" v-model="form.Recommend" :checked="form.Recommend==='推薦'" disabled >
                  <label for="Recommend">推薦</label>
                  <input type="radio" id="notRecommend" value="不推薦" v-model="form.Recommend" :checked="form.Recommend==='不推薦'" disabled>
                  <label for="notRecommend">不推薦</label>
                </div>
              </div>
        <div class="form-group_s">
            <label style="background-color: #e7e3e3; font-weight: bold;">居住安全自主檢視資料(學生填寫)</label>
            <br>
            <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">木造隔間及鐵皮加蓋</label>
                <div class="radio-options_s">
                    <input type="radio" id="woodYes" value="是" v-model="form.woodStructure" :checked="form.woodStructure === '是'" disabled>
                    <label for="woodYes">是</label>
                    <input type="radio" id="woodNo" value="否" v-model="form.woodStructure" :checked="form.woodStructure === '否'" disabled>
                    <label for="woodNo">否</label>
                </div>
            </div>
            <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">有火警警報器或偵煙器</label>
                <div class="radio-options_s">
                    <input type="radio" id="fireYes" value="是" v-model="form.fireAlarm" :checked="form.fireAlarm === '是'" disabled>
                    <label for="fireYes">是</label>
                    <input type="radio" id="fireNo" value="否" v-model="form.fireAlarm" :checked="form.fireAlarm === '否'" disabled>
                    <label for="fireNo">否</label>
                </div>
            </div>
            <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">逃生通道暢通且標示清楚</label>
                <div class="radio-options_s">
                    <input type="radio" id="hallwayYes" value="是" v-model="form.escapeRoute" :checked="form.escapeRoute === '是'" disabled>
                    <label for="hallwayYes">是</label>
                    <input type="radio" id="hallwayNo" value="否" v-model="form.escapeRoute" :checked="form.escapeRoute === '否'" disabled>
                    <label for="hallwayNo">否</label>
                </div>
            </div>
            <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">門鎖及鎖具是否管理良好</label>
                <div class="radio-options_s">
                    <input type="radio" id="lockYes" value="是" v-model="form.lockManagement" :checked="form.lockManagement === '是'" disabled>
                    <label for="lockYes">是</label>
                    <input type="radio" id="lockNo" value="否" v-model="form.lockManagement" :checked="form.lockManagement === '否'" disabled>
                    <label for="lockNo">否</label>
                </div>
            </div>
            <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">有安裝照明設備</label>
                <div class="radio-options_s">
                    <input type="radio" id="lightYes" value="是" v-model="form.lighting" :checked="form.lighting === '是'" disabled>
                    <label for="lightYes">是</label>
                    <input type="radio" id="lightNo" value="否" v-model="form.lighting" :checked="form.lighting === '否'" disabled>
                    <label for="lightNo">否</label>
                </div>
            </div>
            <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">了解及熟悉電路安全及逃生要領</label>
                <div class="radio-options_s">
                    <input type="radio" id="electricYes" value="是" v-model="form.circuitSafety" :checked="form.circuitSafety === '是'" disabled>
                    <label for="electricYes">是</label>
                    <input type="radio" id="electricNo" value="否" v-model="form.circuitSafety" :checked="form.circuitSafety === '否'" disabled>
                    <label for="electricNo">否</label>
                </div>
            </div>
            <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">了解派出所及消防隊等專線電話</label>
                <div class="radio-options_s">
                    <input type="radio" id="policeYes" value="是" v-model="form.emergencyContacts" :checked="form.emergencyContacts === '是'" disabled>
                    <label for="policeYes">是</label>
                    <input type="radio" id="policeNo" value="否" v-model="form.emergencyContacts" :checked="form.emergencyContacts === '否'" disabled>
                    <label for="policeNo">否</label>
                </div>
            </div>
            <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">使用多種電器是否插在同一條延長線</label>
                <div class="radio-options_s">
                    <input type="radio" id="electricEquipmentYes" value="是" v-model="form.electricEquipment" :checked="form.electricEquipment === '是'" disabled>
                    <label for="electricEquipmentYes">是</label>
                    <input type="radio" id="electricEquipmentNo" value="否" v-model="form.electricEquipment" :checked="form.electricEquipment === '否'" disabled>
                    <label for="electricEquipmentNo">否</label>
                </div>
            </div>
            <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">有滅火器且功能正常</label>
                <div class="radio-options_s">
                    <input type="radio" id="hydrantYes" value="是" v-model="form.fireExtinguisher" :checked="form.fireExtinguisher === '是'" disabled>
                    <label for="hydrantYes">是</label>
                    <input type="radio" id="hydrantNo" value="否" v-model="form.fireExtinguisher" :checked="form.fireExtinguisher === '否'" disabled>
                    <label for="hydrantNo">否</label>
                </div>
            </div>
            <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">熱水器安全良好</label>
              
                <div class="radio-options_s">
                  <input type="radio" id="hotWaterYes" value="是" v-model="form.hotWater" :checked="form.hotWater==='是'" disabled>
                  <label for="hotWaterYes">是</label>
                  <input type="radio" id="hotWaterNo" value="否" v-model="form.hotWater" :checked="form.hotWater==='否'" disabled>
                  <label for="hotWaterNo">否</label>
                </div>
              </div>
      
              <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">分六個房間以上或十個床位以上</label>
              
                <div class="radio-options_s">
                  <input type="radio" id="roomBedYes" value="是" v-model="form.roomBed" :checked="form.roomBed==='是'" disabled >
                  <label for="roomBedYes">是</label>
                  <input type="radio" id="roomBedNo" value="否" v-model="form.roomBed" :checked="form.roomBed==='否'" disabled>
                  <label for="roomBedNo">否</label>
                </div>
              </div>
              <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">有安裝監視器</label>
              
                <div class="radio-options_s">
                  <input type="radio" id="CCTVYes" value="是" v-model="form.CCTV" :checked="form.CCTV==='是'" disabled>
                  <label for="CCTVYes">是</label>
                  <input type="radio" id="CCTVNo" value="否" v-model="form.CCTV" :checked="form.CCTV==='否'" disabled>
                  <label for="CCTVNo">否</label>
                </div>
              </div>
              <div class="radio-group_s">
                <label for="visitDetails" style="font-weight: bold;">符合內政部政策</label>
              
                <div class="radio-options_s">
                  <input type="radio" id="lawYes" value="是" v-model="form.law" :checked="form.law==='是'" disabled>
                  <label for="lawYes">是</label>
                  <input type="radio" id="lawNo" value="否" v-model="form.law" :checked="form.law==='否'" disabled>
                  <label for="lawNo">否</label>
                </div>
              </div>
        </div>
    </div>
          <div class="form-group">
            <label style="background-color: #e7e3e3; font-weight: bold;">環境與情況評估(導師填寫)</label>
            <br>
            <div class="radio-group">
              <label for="visitDetails" style="font-weight: bold;">押金要求</label>
              
              <div class="radio-options" style="margin-left: 25px;"> 
                <input type="radio" id="depositYes" value="合理" v-model="form2.deposit" :checked="form2.deposit === '合理'" disabled>
                <label for="depositYes">合理</label>
                <input type="radio" id="depositNo" value="不合理" v-model="form2.deposit" :checked="form2.deposit === '不合理'" disabled>
                <label for="depositNo">不合理(2個月以上之租金)</label>
                
              </div>
            </div>
            <div class="radio-group">
                <label for="bill" style="font-weight: bold;">水電費要求</label>
                <div class="radio-options">
                    <input type="radio" id="billYes" value="合理" v-model="form2.bill" :checked="form2.bill === '合理'" disabled>
                    <label for="billYes">合理</label>
                    <input type="radio" id="billNo" value="不合理" v-model="form2.bill" :checked="form2.bill === '不合理'" disabled>
                    <label for="billNo">不合理</label>
                </div>
            </div>
            
            <div class="radio-group">
                <label for="environment" style="font-weight: bold;">居家環境</label>
                <div class="radio-options">
                    <input type="radio" id="environmentYes" value="佳" v-model="form2.environment" :checked="form2.environment === '佳'" disabled> 
                    <label for="environmentYes">佳</label>
                    <input type="radio" id="environmentMid" value="適中" v-model="form2.environment" :checked="form2.environment === '適中'" disabled> 
                    <label for="environmentMid">適中</label>
                    <input type="radio" id="environmentBad" value="欠佳" v-model="form2.environment" :checked="form2.environment === '欠佳'" disabled> 
                    <label for="environmentBad">欠佳，說明</label>
                    <input type="text" id="environmentDetails" v-model="form2.environmentDetails" :checked="form2.environment !== '欠佳'" disabled>

                </div>
            </div>
            
            <div class="radio-group">
                <label for="facilities" style="font-weight: bold;">生活設施</label>
                <div class="radio-options"> 
                    <input type="radio" id="facilitiesYes" value="佳" v-model="form2.facilities" :checked="form2.facilities === '佳'" disabled> 
                    <label for="facilitiesYes">佳</label>
                    <input type="radio" id="facilitiesMid" value="適中" v-model="form2.facilities" :checked="form2.facilities === '適中'" disabled> 
                    <label for="facilitiesMid">適中</label>
                    <input type="radio" id="facilitiesBad" value="欠佳" v-model="form2.facilities" :checked="form2.facilities === '欠佳'" disabled> 
                    <label for="facilitiesBad">欠佳，說明</label>
                    <input type="text" id="facilitiesDetails" v-model="form2.facilitiesDetails" :checked="form2.facilities !== '欠佳'" disabled>
                </div>
            </div>
            
            <div class="radio-group">
                <label for="visitStatus" style="font-weight: bold;">訪視現況</label>
                <div class="radio-options">
                    <input type="radio" id="visitStatus1" value="良好" v-model="form2.visitStatus" :checked="form2.visitStatus === '良好'" disabled> 
                    <label for="visitStatus1">良好</label>
                    <input type="radio" id="visitStatus2" value="適中" v-model="form2.visitStatus" :checked="form2.visitStatus === '適中'" disabled> 
                    <label for="visitStatus2">適中</label>
                    <input type="radio" id="visitStatus3" value="待加強" v-model="form2.visitStatus" :checked="form2.visitStatus === '待加強'" disabled>
                    <label for="visitStatus3">待加強，說明</label>
                    <input type="text" id="visitStatusDetails" v-model="form2.visitStatusDetails" :checked="form2.visitStatus !== '待加強'" disabled>
                </div>
            </div>
            
            <div class="radio-group">
                <label for="well" style="font-weight: bold;">主客相處</label>
                <div class="radio-options"> 
                    <input type="radio" id="well1" value="良好" v-model="form2.well" :checked="form2.well === '良好'" disabled>
                    <label for="well1">良好</label>
                    <input type="radio" id="well2" value="待加強" v-model="form2.well" :checked="form2.well === '待加強'" disabled>
                    <label for="well2">待加強</label>
                </div>
            </div>
            
            <label style="background-color: #e7e3e3; font-weight: bold;">訪視結果(導師填寫)</label>
            <div class="radio-group">
                <div class="radio-options">
                    <input type="radio" id="visitResult1" value="整體租賃狀況良好" v-model="form2.visitResult" :checked="form2.visitResult === '整體租賃狀況良好'" disabled> 
                    <label for="visitResult1">整體租賃狀況良好</label>
                    <input type="radio" id="visitResult2" value="聯繫家長關注" v-model="form2.visitResult" :checked="form2.visitResult === '聯繫家長關注'" disabled> 
                    <label for="visitResult2">聯繫家長關注</label>
                    <input type="radio" id="visitResult3" value="安全堪慮請協助" v-model="form2.visitResult" :checked="form2.visitResult === '安全堪慮請協助'" disabled> 
                    <label for="visitResult3">安全堪慮請協助</label>
                    <input type="radio" id="visitResult4" value="其他" v-model="form2.visitResult" :checked="form2.visitResult === '其他'" disabled>
                    <label for="visitResult4">其他，說明:</label>
                    <input type="text" id="visitResultDetails" v-model="form2.visitResultDetails" :checked="form2.visitResult !== '其他'" disabled>
                </div>
            </div>
            
            <div class="input-label-wrapper">
                <label>其他記載或建議事項:</label>
                <input type="text" id="visitResultOthers" v-model="form2.visitResultOthers" disabled>
            </div>
            
          </div>
           
        </form>
      </div>
      
    </main>

  </div>
</template>

<script setup>
  import axios from 'axios';
 
</script>
<script>
export default {
  data() {
    return {
      form: {},
      form2: {},
      formSubmitted: false,
    };
  },
  created() {
    this.getStuRecordInfo(this.$route.params.id, this.$route.params.grade, this.$route.params.semester);
   
    
  },
  methods:{
    getStuRecordInfo(id,year,semester) {
      const path = `http://localhost:5000/get_StuRecord/${id}/${year}/${semester}`;
      axios.get(path)
        .then((res) => {
          this.form = res.data.stuRecord_info[0];
          this.form.studentName = this.$route.params.name;
          this.getTeaRecordInfo(this.$route.params.id, this.$route.params.grade, this.$route.params.semester,this.$route.params.tid);
        })
        .catch((error) => {
          this.getTeaRecordInfo(this.$route.params.id, this.$route.params.grade, this.$route.params.semester,this.$route.params.tid);
          console.error(error);
        });
    },
    getTeaRecordInfo(id,year,semester,tid) {
      const path = `http://localhost:5000/get_TeaRecord/${id}/${year}/${semester}/${tid}`;
      axios.get(path)
        .then((res) => {
          this.form2 = res.data.teaRecord_info[0];
        })
        .catch((error) => {
          console.error(error);
        });
    },
  }
 
};
</script>
<style scoped>
body {
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
      background-color: #f1f1f1;
      min-width: 160px;
      box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
      z-index: 1;
    }
    .dropdown-content a {
      color: #333;
      padding: 12px 16px;
      text-decoration: none;
      display: block;
    }
    .dropdown-content a:hover {
      background-color: #ddd;
    }
    .dropdown:hover .dropdown-content {
      display: block;
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
        margin-left: 10px; /* Reset margin-left */
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
    
        .radio-group_s {
            margin-bottom: 1em;
        }
        .radio-options_s {
            display: flex;
            align-items: center;
        }
        .radio-options_s input[type="radio"] {
            margin-left: 18em;
            margin-right: 0.1em;
        }
        .radio-options_s label {
            margin-right: 1em;
        }
        .form-group_s label {
      display: block;
      margin-bottom: 5px;
      text-align: left;
    }
    
    

</style>
