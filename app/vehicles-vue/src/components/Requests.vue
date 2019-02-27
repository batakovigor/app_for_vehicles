<template>
    <div>
        <el-table
            ref="filterTable"
            :data=tableData
            style="width: 100%"
            :row-class-name="tableRowClassName"
            @row-dblclick="dialogFormVisible = true">
            <el-table-column
                prop="car_model"
                label="Марка АТС"
                sortable
                width="150">
            </el-table-column>
            <el-table-column
                prop="gos_nomer"
                label="Гос.номер"
                width="100">
            </el-table-column>
            <el-table-column
                prop="type_car"
                label="Тип АТС"
                width="150">
            </el-table-column>
            ing
            <el-table-column
                prop="department"
                label="Подразделение"
                sortable
                :filters="departments"
                :filter-method="filterHandler"
                width="180">
            </el-table-column>
            <el-table-column label="Время подачи АТС">
                <el-table-column
                    prop="time_start_request"
                    label="с"
                    width="80">
                </el-table-column>
                <el-table-column
                    prop="time_end_request"
                    label="по"
                    width="80">
                </el-table-column>
            </el-table-column>
            <el-table-column
                prop="description"
                label="Пункт назначения">
            </el-table-column>
            <el-table-column
                prop="comment"
                label="Примечания">
            </el-table-column>
        </el-table>


        <!-- Form -->

        <el-dialog title="Заявка" :visible.sync="dialogFormVisible">
            <el-form :rules="rulesRequest" ref="refFormRequest" :model="ruleFormRequest" label-width="120px">

                    <el-form-item label="Тип заявки" prop="type_request">
                        <el-select v-model="ruleFormRequest.value" clearable placeholder="Выберите тип заявки" style="width: 100%;">
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
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Requests",
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
                rulesRequest:{
                    type_request: [
                        { required: true, message: 'Пожалйуста выберите тип заявки', trigger: 'change' }
                    ],
                    car: [
                        { required: true, message: 'Пожалйуста выберите автомобиль', trigger: 'change' }
                    ]
                },
                formLabelWidth: '120px',
                tableData: [],
                departments: []
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem("auth_token")},
            });
            this.loadRequests()
            this.loadDepartmentsComboFilter()
            this.loadTypeRequestComboSelect()
        },
        methods: {
            loadRequests() {
                var records = []
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/vehicles/requests/",
                    type: "GET",
                    success: (response) => {
                        $.each(response.data.data, function (index, value) {
                            var obj = {
                                id: value.id,
                                type_request: value.type_request.name,
                                car_model: value.car.car_model.name,
                                gos_nomer: value.car.gos_nomer,
                                type_car: value.car.type_car.name,
                                department: value.department.name,
                                time_start_request: value.time_start_request,
                                time_end_request: value.time_end_request,
                                description: value.description,
                                comment: value.comment
                            }
                            records[index] = obj
                        })
                        this.tableData = records
                    }
                })
            },
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
            loadDepartmentsComboFilter() {
                var dep = []
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/vehicles/filter-departments/",
                    type: "GET",
                    success: (response) => {
                        $.each(response.data, function (index, value) {
                            var obj = {
                                text:value,
                                value:value
                            }
                            dep[index] = obj
                        })
                        //console.log(response.data)
                        this.departments = dep
                    }
                })
            },
            tableRowClassName({row, rowIndex}) {
                if (rowIndex === 1) {
                    return 'warning-row';
                } else if (rowIndex === 3) {
                    return 'success-row';
                }
                return '';
            },
            filterHandler(value, row, column) {
                const property = column['property'];
                return row[property] === value;
            },
            RowDblClick(row, rowIndex){
                console.log(row)
            },
            handleOpen(key, keyPath) {
                console.log(key, keyPath);
            },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
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
    .el-table .warning-row {
        background: oldlace;
    }

    .el-table .success-row {
        background: #f0f9eb;
    }

    .el-main {
        background-color: #E9EEF3;
        color: #333;
        text-align: center;

    }
</style>
