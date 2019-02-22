<template>
    <div>
        <el-row type="flex">
            <el-col :span="24">
                <div class="grid-content">
                    <div>
                        <el-table
                            ref="filterTable"
                            :data=tableData
                            style="width: 100%"
                            :row-class-name="tableRowClassName"
                            @row-dblclick="Alert('1')">
                            <el-table-column
                                prop="car.car_model.name"
                                label="Марка АТС"
                                sortable
                                width="150">
                            </el-table-column>
                            <el-table-column
                                prop="car.gos_nomer"
                                label="Гос.номер"
                                width="100">
                            </el-table-column>
                            <el-table-column
                                prop="car.type_car.name"
                                label="Тип АТС"
                                width="150">
                            </el-table-column>ing
                            <el-table-column
                                prop="department.name"
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
                    </div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Requests",
        data() {
            return {
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
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/vehicles/requests/",
                    type: "GET",
                    success: (response) => {
                        this.tableData = response.data.data
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

    .el-menu-vertical-demo:not(.el-menu--collapse) {
        width: 200px;
        min-height: 400px;
    }

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
