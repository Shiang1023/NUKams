<script setup>
</script>

<template>
    <body class="bg-gray-100">
        <header class="bg-blue-600 text-white p-4">
            <div class="container mx-auto flex justify-between items-center">
                <h1 class="text-2xl font-bold">Nukams</h1>
                <nav>
                    <ul class="flex space-x-4">
                        <li><Routerlink to="/">Home</Routerlink></li>
                        <li><Routerlink to="/">About</Routerlink></li>
                        <li><Routerlink to="/">Contact</Routerlink></li>
                    </ul>
                </nav>
            </div>
        </header>
    

        <div class="container mx-auto mt-4 flex">
            <main class="flex-1 bg-white p-6 rounded-lg shadow-lg">
                <RouterView name="main"></RouterView>
            </main>
            <aside class="w-80 bg-white p-6 rounded-lg shadow-lg">
                <div class="bg-white p-4 rounded-lg shadow-lg mb-4">
                    <h2 class="text-lg font-bold">Advertisement</h2>
                    <p>Some content here</p>
                </div>
                <div class="bg-white p-4 rounded-lg shadow-lg">
                    <h2 class="text-lg font-bold">Post</h2>
                    <p>Some content here</p>
                </div>
                <div class="bg-white p-4 rounded-lg shadow-lg">
                    <h2 class="text-lg font-bold">Post</h2>
                    <p>Some content here</p>
                </div>
            </aside>
        </div>
    </body>
</template>