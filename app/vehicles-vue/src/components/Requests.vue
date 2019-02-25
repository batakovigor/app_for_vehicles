<template>
    <el-main>
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

        <el-dialog title="Shipping address" :visible.sync="dialogFormVisible">
            <el-form :model="form">
                <el-form-item label="Promotion name" :label-width="formLabelWidth">
                    <el-input v-model="form.name" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="Zones" :label-width="formLabelWidth">
                    <el-select v-model="form.region" placeholder="Please select a zone">
                        <el-option label="Zone No.1" value="shanghai"></el-option>
                        <el-option label="Zone No.2" value="beijing"></el-option>
                    </el-select>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">Отмена</el-button>
            <el-button type="primary" @click="dialogFormVisible = false">Сохранить</el-button>
        </span>
        </el-dialog>
    </el-main>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Requests",
        data() {
            return {
                dialogFormVisible: false,
                form: {

                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: ''
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
