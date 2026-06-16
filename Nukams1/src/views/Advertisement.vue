<template>
  <!-- back to last page -->
  <div style="background-color: rgb(213, 222, 226);">
    <button @click="$router.go(-1)">返回</button>
    <button v-if="IsLandLord" @click="$router.push({ name: 'AddAd', params: { username: route.params.username } })">新增</button>
    <button v-if="IsLandLord" @click="MyTrigger">Myself</button>
    <div class="rental-listing">
      <Select
        id="price-filter"
        label="篩選價格"
        :options="priceOptions"
        v-model="selectedPrice"
      />
      <div class="flex justify-around flex-col">
        <label for="min-price">最低價格:</label>
        <input type="text" id="min-price" v-model="minPriceText" style="border:2px #ccc solid; height: 40px; margin-bottom: 10px;" />
        <label for="max-price">最高價格:</label>
        <input type="text" id="max-price" v-model="maxPriceText" style="border:2px #ccc solid; height: 40px;margin-bottom: 10px;" />
      </div>
      <Card v-for="(rental, index) in filteredRentals" :key="index" :MY="MY" :AD_id="rental.ad_id" class="rental-card">
        <template #header>
          <div>
            <h2 class="font-bold">{{ rental.title }}</h2>
            <p>{{ rental.description }}</p>
          </div>
        </template>
        <template #content>
          <div class="rental-content">
            <img :src="publicPath + rental.image" alt="Rental Image" class="rental-image" />
            <div class="rental-details">
              <p>房租價格: {{ rental.price }}</p>
              <p>地址: {{ rental.address }}</p>
              <p>房東電話: {{ rental.phone }}</p>
            </div>
            <button v-if="MY" @click="showEditModal(rental)">修改</button>
            <button v-if="MY" @click="deleteAd(rental)">刪除</button>
          </div>
        </template>
      </Card>
    </div>
    <EditModal
      v-if="showModal"
      :show="showModal"
      :rental="currentRental"
      :onClose="closeModal"
      :onSave="saveAd"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import Card from '../components/card.vue'
import Select from '../components/Select.vue'
import EditModal from '../components/EditModal.vue'

const publicPath = '/pic/AD/'
const rentals = ref([]);
const user = ref('test');
const route = useRoute()
const priceOptions = ref([
  { value: '', text: '所有價格' },
  { value: '2000-4000', text: 'NT$ 2,000 - NT$ 4,000/月' },
  { value: '4000-6000', text: 'NT$ 4,000 - NT$ 6,000/月' },
  { value: '6000-8000', text: 'NT$ 6,000 - NT$ 8,000/月' },
  { value: '8000-10000', text: 'NT$ 8,000 - NT$ 10,000/月' },
  { value: '10000-13000', text: 'NT$ 10,000 - NT$ 13,000/月' },
  { value: '13000-18000', text: 'NT$ 13,000 - NT$ 18,000/月' },
])

const selectedPrice = ref('')
const minPriceText = ref('')
const maxPriceText = ref('')
const MY = ref(false);
const IsLandLord = ref(false)
const showModal = ref(false)
const currentRental = ref(null)

onMounted(async () => {
  console.log('Component mounted')
  const response = await axios.get('http://localhost:5000/api/advertisement');
  rentals.value = response.data.data;
  const role = JSON.parse(localStorage.getItem('role'));
  console.log(role)
  if (role === '房東') {
    IsLandLord.value = true
  }
});

onUnmounted(() => {
  console.log('Component unmounted')
})

const filteredRentals = computed(() => {
  if (IsLandLord.value && MY.value) {
    return Myself()
  }
  if (!selectedPrice.value && (minPriceText.value === '' || maxPriceText.value === '')) {
    return rentals.value
  }
  if (selectedPrice.value) {
    const [minPrice, maxPrice] = selectedPrice.value.split('-').map(price => parseInt(price, 10))
    return rentals.value.filter(rental => {
      const rentalPrice = rental.price
      return rentalPrice >= minPrice && rentalPrice <= maxPrice
    })
  } else {
    const MinPrice = parseInt(minPriceText.value.replace(/[^0-9]/g, ''))
    const MaxPrice = parseInt(maxPriceText.value.replace(/[^0-9]/g, ''))
    return rentals.value.filter(rental => {
      const rentalPrice = rental.price
      return rentalPrice >= MinPrice && rentalPrice <= MaxPrice
    })
  }
})

const MyTrigger = () => {
  MY.value = !MY.value
}

const Myself = () => {
  const username = route.params.username
  if (username && IsLandLord.value) {
    return rentals.value.filter(rental => rental.landlord === username)
  }
}

const deleteAd = (rentals) => {
  axios.get(`http://localhost:5000/api/delete_advertisement/${rentals.ad_id}`)
    .then(response => {
      rentals.value = rentals.value.filter(rental => rental.ad_id !== rentals.ad_id);
    })
    .catch(error => {
      console.error(error);
    });
    window.location.reload();
}

const showEditModal = (rental) => {
  currentRental.value = rental
  showModal.value = true
}

const closeModal = () => {
  showModal.value = false
}

const saveAd = (updatedRental) => {
  const index = rentals.value.findIndex(rental => rental.ad_id === updatedRental.ad_id)
  if (index !== -1) {
    rentals.value[index] = updatedRental
  }
  alert('已更新')
}

</script>

<style scoped>
.rental-listing {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 20px;
  color: black;
}

.rental-card {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 20px;
  border: 1px solid #3e4986;
  border-radius: 8px;
}

.rental-content {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 20px;
}

.rental-image {
  width: 300px;
  height: 200px;
  object-fit: cover;
  border-radius: 8px;
}

.rental-details {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 60%;
  /* 字體大小 */
  font-size: 1.2em;
}

button {
  background-color: rgb(22, 55, 69);
  color: rgb(255, 255, 255);
  font-size: large;
  font-weight: bold;
  font-family: 'Times New Roman', Times, serif;
  padding: 14px 20px;
  margin: 20px;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  width: 10%;
  max-height: 56.8px;
}

button:hover {
  background-color: rgb(23, 46, 56);
  color: rgb(213, 222, 226);
}
</style>
