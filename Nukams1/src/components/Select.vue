<template>
    <div class="select-container">
      <label :for="id" class="select-label">{{ label }}</label>
      <select :id="id" v-model="selectedValue" @change="handleChange" class="select-element">
        <option v-for="option in options" :key="option.value" :value="option.value">
          {{ option.text }}
        </option>
      </select>
    </div>
  </template>
  
  <script setup>
  import { defineProps, defineEmits, ref, watch } from 'vue'
  
  const props = defineProps({
    id: {
      type: String,
      required: true,
    },
    label: {
      type: String,
      required: true,
    },
    options: {
      type: Array,
      required: true,
    },
    modelValue: {
      type: String,
      required: true,
    },
  })
  
  const emits = defineEmits(['update:modelValue'])
  
  const selectedValue = ref(props.modelValue)
  
  watch(selectedValue, (newValue) => {
    emits('update:modelValue', newValue)
  })
  
  const handleChange = () => {
    emits('update:modelValue', selectedValue.value)
  }
  </script>
  
  <style scoped>
  .select-container {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
  }
  
  .select-label {
    margin-bottom: 5px;
    font-weight: bold;
  }
  
  .select-element {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  </style>