<template>
        <el-container>
            <el-header>Зяавки на автотранспорт
                <div class="line"></div>
            </el-header>
            <div class="line"></div>
            <el-breadcrumb separator-class="el-icon-arrow-right">
                <el-breadcrumb-item :to="{ path: '/' }">homepage</el-breadcrumb-item>
                <el-breadcrumb-item>promotion management</el-breadcrumb-item>
                <el-breadcrumb-item>promotion list</el-breadcrumb-item>
                <el-breadcrumb-item>promotion detail</el-breadcrumb-item>
            </el-breadcrumb>
            <div class="line"></div>
            <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
                <el-menu-item index="1">На домашнюю</el-menu-item>
                <el-submenu index="2">
                    <template slot="title">Заявки</template>
                    <el-menu-item index="2-1">на легковой автотранспорт</el-menu-item>
                    <el-menu-item index="2-2">на спецтехнику</el-menu-item>
                    <el-submenu index="2-4">
                        <template slot="title">item four</template>
                        <el-menu-item index="2-4-1">item one</el-menu-item>
                        <el-menu-item index="2-4-2">item two</el-menu-item>
                        <el-menu-item index="2-4-3">item three</el-menu-item>
                    </el-submenu>
                </el-submenu>
                <el-menu-item index="3" disabled>Info</el-menu-item>
                <el-button type="primary" v-if="!auth" @click="gologin">Вход</el-button>
                <el-button type="primary" v-else @click="logout">Выход</el-button>
            </el-menu>
            <div class="line"></div>
            <el-main>
                <Requests v-if="auth"></Requests>
            </el-main>
        </el-container>
</template>

<script>
    import Requests from '@/components/Requests'
    export default {
        name: "Home",
        components:{
            Requests
        },
        data() {
            return {
                activeIndex: '1',
                activeIndex2: '1'
            };
        },
        computed: {
            auth() {
                if(sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods:{
            gologin() {
                this.$router.push({name: "login"})
            },
            logout() {
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            },
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            }
        },
    }
</script>

<style>
    .el-header, .el-footer {
        background-color: #B3C0D1;
        color: #333;
        text-align: center;
        line-height: 60px;
    }

    body > .el-container {
        margin-bottom: 40px;
    }

</style>
