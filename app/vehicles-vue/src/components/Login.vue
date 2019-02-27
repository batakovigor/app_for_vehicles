<template>
    <el-container>
        <el-form label-width="150px">
            <el-form-item label="Имя пользователя" prop="name">
                <el-input v-model="login" type="text" placeholder="Логин"></el-input>
            </el-form-item>
            <el-form-item label="Пароль" prop="pass">
                <el-input v-model="password" type="password" autocomplete="off" placeholder="Пароль"></el-input>
            </el-form-item>
            <el-button type="primary" @click="setlogin">Войти</el-button>
        </el-form>
    </el-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Login",
        data(){
            return{
                login: '',
                password: '',
            }
        },
        methods: {
            setlogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/create/",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if(response.status === 400) {
                            alert("Логин или пароль не верен.")
                        }
                        console.log(response)
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
