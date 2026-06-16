<template>
  <div>
   
    <div class="VRM_main">
      <button class="VRM" @click="goToTestPage('editRecordSelectName', 'T10912')">學生基本資料</button>
      <button class="VRM" @click="goToTestPage('fillRecordSelectName', 'T10912')">學生住宿資料</button>
    </div>

  </div>
</template>

<script setup>
import Up from '../components/Up.vue'
import Down from '../components/Down.vue'
import Tcs_nav from '@/components/Tcs_nav.vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const goToTestPage = (page, id) => {
  router.push({ name: page, params: { id } });
};
</script>

<style scoped>
/* Global styles */
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
/* Main section styles */
.VRM_main {
  display: flex;

  
  justify-content: center;
  align-items: center;
  padding: 20px;
  text-align: center;
}

/* Button styles */
.VRM {
  display: inline-block;
  font-size: 1.2em;
  margin: 10px;
  padding: 10px 20px;
  color: #000;
  background-color: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 150px;
}

.VRM:hover {
  background-color: #8d8a8a; /* Slightly darker background on hover */
}

/* Footer styles */

</style>