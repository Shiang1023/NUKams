<template>
    <div v-if="show" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h2>修改廣告</h2>
        <form @submit.prevent="updateAd" class="modal-form">
          <label for="title">標題:</label>
          <input type="text" id="title" v-model="newTitle" required>
  
          <label for="description">内容:</label>
          <input type="text" id="description" v-model="newDescription" required>
  
          <label for="price">價格:</label>
          <input type="text" id="price" v-model="newPrice" required>
  
          <label for="address">地址:</label>
          <input type="text" id="address" v-model="newAddress" required>
  
          <button type="submit">保存</button>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue'
  import axios from 'axios'

  // 定義 props
  const props = defineProps({
    show: Boolean,
    rental: Object,
    onClose: Function,
    onSave: Function 
  })
  
  // 初始化表單數據
  const newTitle = ref(props.rental.title)
  const newDescription = ref(props.rental.description)
  const newPrice = ref(props.rental.price)
  const newAddress = ref(props.rental.address)
  
  // 監聽 props.rental 的變化
  watch(() => props.rental, (newVal) => {
    if (newVal) {
      newTitle.value = newVal.title
      newDescription.value = newVal.description
      newPrice.value = newVal.price
      newAddress.value = newVal.address
    }
  }, { immediate: true })
  
  // 關閉模態框
  const closeModal = () => {
    props.onClose()
  }
  
  // 更新廣告信息
  const updateAd = () => {
    const updatedRental = {
      ...props.rental,
      title: newTitle.value,
      description: newDescription.value,
      price: newPrice.value,
      address: newAddress.value,
    }
    if (!/^\d+$/.test(newPrice.value)) {
      alert('價格必須為数字')
      return
    }
    try {
    // console.log('更新廣告', updatedRental.id, newTitle.value, newDescription.value, newPrice.value, newAddress.value)
    const response = axios.get(`http://localhost:5000/api/advertisement/update_advertisement/${updatedRental.ad_id},${newTitle.value},${newDescription.value},${newPrice.value},${newAddress.value}`)
    console.log('廣告更新成功', response.data)
    props.onSave(updatedRental)
    closeModal()
  } catch (error) {
    console.error('廣告更新失敗', error)
  }
  }
  </script>
  
  <style scoped>
  .modal {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1000;
  }
  
  .modal-content {
    background-color: #fff;
    padding: 30px;
    border-radius: 10px;
    width: 90%;
    max-width: 500px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    position: relative;
    animation: slide-down 0.3s ease-out;
  }
  
  .modal-content h2 {
    margin-top: 0;
    font-size: 1.5em;
    color: #333;
    text-align: center;
  }
  
  .modal-form {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .modal-form label {
    font-weight: bold;
    margin-bottom: 5px;
    color: #555;
  }
  
  .modal-form input {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1em;
    width: 100%;
  }
  
  .modal-form button {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 5px;
    font-size: 1em;
    cursor: pointer;
    margin-top: 10px;
  }
  
  .modal-form button:hover {
    background-color: #2980b9;
  }
  
  .close {
    position: absolute;
    top: 15px;
    right: 15px;
    font-size: 1.5em;
    cursor: pointer;
    color: #999;
  }
  
  @keyframes slide-down {
    from {
      transform: translateY(-200px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }
  </style>
  