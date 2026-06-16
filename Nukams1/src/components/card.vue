<template>
    <div class="card">
      <div class="card-header">
        <slot name="header"></slot>
        <!-- 檢舉 only in advertisement-->
        <button v-if="inAD && !MY" class="report" @click="report">檢舉</button>
      </div>
      <div class="card-content">
        <slot name="content"></slot>
      </div>
      <div class="card-footer">
        <slot name="footer"></slot>
      </div>
    </div>
  </template>
  
<script setup>
import { ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
const props = defineProps({
  MY: {
    type: Boolean,
    required: false,
  },
  AD_id: {
    type: String,
    required: false,
  }

});
const route = useRoute();

// 判斷當前路由是否是 advertisement
const inAD = route.name === 'advertisement';

function report(){
  alert('檢舉成功')
  const path = `http://127.0.0.1:5000/api/update_report_to_one/${props.AD_id},advertisement`;
  axios.get(path)
    .then((res) => {
      console.log("succeed");
    })
    .catch((error) => {
      console.error(error);
    });
  }
</script>

<style scoped>
.card {
  color: black;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 20px;
  margin: 10px 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
}

.card-header,
.card-content,
.card-footer {
  margin-bottom: 10px;
}
.card-content {
  display: flex;
  width: 100%;
  flex-direction: row;
  justify-content: space-between;
}
.card-header {
  font-weight: bold;
  font-size: 1.2em;
  width: 100%;
  display: flex;
  justify-content: space-between;

}

.card-footer {
  text-align: right;
  font-size: 0.9em;
  color: #666;
}
.report{
  background-color: #fa761e98;
  color: white;
  font-size: 1em;
  font-weight: bold;
  font-family: 'Times New Roman', Times, serif;
  padding: 5px 10px;
  border: none;
  border-radius: 30px;
  cursor: pointer;
}
.report:hover{
  background-color: #b46936;
}
</style>
