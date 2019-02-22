<template>
    <div>
        <div>
            <el-row>
                <el-col :span="24">
                    <div class="grid-content">
                        <h1>
                            Зяавки на автотранспорт
                        </h1>
                        <button v-if="!auth" @click="gologin">Вход</button>
                        <button v-else @click="logout">Выход</button>
                        <Requests v-if="auth"></Requests>
                    </div>
                </el-col>
            </el-row>
        </div>

    </div>
</template>

<script>
    import Requests from '@/components/Requests'
    export default {
        name: "Home",
        components:{
            Requests
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
            }
        },
    }
</script>

<style scoped>
    .el-row {
        margin-bottom: 20px;
        &:last-child {
            margin-bottom: 0;
        }
    }

    .el-col {
        border-radius: 4px;
    }

    .bg-purple-dark {
        background: #99a9bf;
    }

    .bg-purple {
        background: #d3dce6;
    }

    .bg-purple-light {
        background: #e5e9f2;
    }

    .grid-content {
        border-radius: 4px;
        min-height: 36px;
    }

    .row-bg {
        padding: 10px 0;
        background-color: #f9fafc;
    }
</style>
