<script setup>
import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <main>
    <router-link to="/loginRegister" class="button">Login</router-link>
  </main>
</template>

<style scoped>
main {
  display: flex;
  place-content: center;
  place-items: center;
  height: 100vh;
  width: 100vw;
  background-color: rgb(76, 85, 95);
}
.button {
  padding: 1rem 2rem;
  background-color: rgb(213, 222, 226);
  color: rgb(19, 68, 60);
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: larger;
  font-weight: bold;
}
.button:hover {
  background-color: rgb(76, 85, 95);
  color: white;
}
</style>