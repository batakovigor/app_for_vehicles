<template>
    <div id="app">

        <router-view/>
    </div>
</template>

<script>
    export default {
        name: 'App'
        // Если токен храниться в localStorage
        // created() {
        //     if(localStorage.getItem("auth_token")) {
        //         $.ajaxSetup({
        //             headers: {'Autorization': "Token " + localStorage.getItem("auth_token")},
        //         });
        //     }
        // }
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
