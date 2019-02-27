<template>
    <el-dialog title="Заявка" :visible.sync="dialogFormVisible">
        <el-form :rules="rulesRequest" ref="refFormRequest" :model="ruleFormRequest" label-width="120px">

            <el-form-item label="Тип заявки" prop="type_request">
                <el-select v-model="ruleFormRequest.value" clearable placeholder="Выберите тип заявки"
                           style="width: 100%;">
                    <el-option
                        v-for="item in ruleFormRequest.type_request"
                        :key="item.value"
                        :label="item.text"
                        :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>

            <el-form-item label="Марка АТС" prop="car">
                <el-select v-model="ruleFormRequest.car" placeholder="Выберите автомобиль" style="width: 100%;">
                    <el-option label="Авто 1" value="Авто 1"></el-option>
                    <el-option label="Авто 2" value="Авто 2"></el-option>
                </el-select>
            </el-form-item>

            <el-form-item label="Activity name">
                <el-input v-model="ruleFormRequest.name"></el-input>
            </el-form-item>

            <el-form-item label="Дата, время подачи АТС" required>
                <el-col :span="8">
                    <el-date-picker type="date" placeholder="Pick a date" v-model="ruleFormRequest.date1"
                                    style="width: 100%;"></el-date-picker>
                </el-col>
                <el-col class="line" :span="1">c</el-col>
                <el-col :span="7">
                    <el-time-picker type="fixed-time" placeholder="Pick a time" v-model="ruleFormRequest.time1"
                                    style="width: 100%;"></el-time-picker>
                </el-col>
                <el-col class="line" :span="1">по</el-col>
                <el-col :span="7">
                    <el-time-picker type="fixed-time" placeholder="Pick a time" v-model="ruleFormRequest.time2"
                                    style="width: 100%;"></el-time-picker>
                </el-col>
            </el-form-item>
            <el-form-item label="Instant delivery">
                <el-switch v-model="ruleFormRequest.delivery"></el-switch>
            </el-form-item>
            <el-form-item label="Activity type">
                <el-checkbox-group v-model="ruleFormRequest.type">
                    <el-checkbox label="Online activities" name="type"></el-checkbox>
                    <el-checkbox label="Promotion activities" name="type"></el-checkbox>
                    <el-checkbox label="Offline activities" name="type"></el-checkbox>
                    <el-checkbox label="Simple brand exposure" name="type"></el-checkbox>
                </el-checkbox-group>
            </el-form-item>
            <el-form-item label="Resources">
                <el-radio-group v-model="ruleFormRequest.resource">
                    <el-radio label="Sponsor"></el-radio>
                    <el-radio label="Venue"></el-radio>
                </el-radio-group>
            </el-form-item>
            <el-form-item label="Activity form">
                <el-input type="textarea" v-model="ruleFormRequest.desc"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitForm('refFormRequest')">Create</el-button>
                <el-button @click="resetForm('refFormRequest')">Reset</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Requestform",
        data() {
            return {
                dialogFormVisible: false,
                ruleFormRequest: {
                    type_request: [],
                    car: '',
                    date1: '',
                    time1: '',
                    time2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: '',
                    value: ''
                },
                rulesRequest: {
                    type_request: [
                        {required: true, message: 'Пожалйуста выберите тип заявки', trigger: 'change'}
                    ],
                    car: [
                        {required: true, message: 'Пожалйуста выберите автомобиль', trigger: 'change'}
                    ]
                },
                formLabelWidth: '120px',
            }
        },
        created() {
            this.loadTypeRequestComboSelect()
        },
        methods: {
            loadTypeRequestComboSelect() {
                var type_req = []
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/vehicles/type-requests/",
                    type: "GET",
                    success: (response) => {
                        $.each(response.data.data, function (index, value) {
                            var obj = {
                                text:value.name,
                                value:value.id
                            }
                            type_req[index] = obj
                        })
                        console.log(type_req)
                        this.ruleFormRequest.type_request = type_req
                    }
                })
            },
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        alert('submit!');
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        }
    }
</script>

<style scoped>

</style>
