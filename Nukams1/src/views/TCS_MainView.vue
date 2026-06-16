<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <body class="bg-gray-100 flex flex-wrap flex-col justify-start item-start w-full">
        <header class="bg-blue-600 p-4 w-full">
            <div class="container mx-auto flex justify-between items-center">
                <h1 class="text-2xl font-bold text-white ">Nukams</h1>
                <nav>
                    <ul class="flex space-x-4 text-blue-600">
                        <li><RouterLink to="">Home</RouterLink></li>
                        <li><RouterLink to="">About</RouterLink></li>
                        <li><RouterLink to="">Contact</RouterLink></li>
                    </ul>
                </nav>
            </div>
        </header>
    

        <div class="container mx-auto my-5 flex flex-1 overflow-hidden">
            <main class="flex-1 bg-white p-6 rounded-lg shadow-lg overflow-y-auto min-w-0">
                <RouterView></RouterView>
            </main>
            <aside class="w-80 bg-white p-6 rounded-lg shadow-lg flex-shrink-0">
                <div class="bg-white p-4 rounded-lg shadow-lg mb-4">
                    <RouterLink :to="{name:'advertisement',params: { id: username }}" class="text-lg font-bold text-blue-600">Advertisement</RouterLink>
                    <p>Some content here</p>
                </div>
                <div class="bg-white p-4 rounded-lg shadow-lg  mb-4">
                    <RouterLink to="/post"class="text-lg font-bold text-blue-600">Post</RouterLink>
                    <p>Some content here</p>
                </div>
                <div class="bg-white p-4 rounded-lg shadow-lg  mb-4">
                    <RouterLink :to="{name:'comment',params: { id: username }}" class="text-lg font-bold text-blue-600">Comment</RouterLink>
                    <p>Some content here</p>
                </div>
            </aside>
        </div>
    </body>
</template>



<style scoped>

    main{
        display: flex;
        flex-direction: column;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    button {
            background-color:  rgb(213, 222, 226);
            color: rgb(26, 36, 85);
            font-size: large;
            font-weight: bold;
            font-family: 'Times New Roman', Times, serif;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            max-height: 56.8px;
            
        }
    
    button:hover {
      background-color: rgb(23, 46, 56);
      color: rgb(213, 222, 226);
    }
</style>