<template>
    <div>
        <el-table
                :data="tableData"
                border
                style="width: 100%"
                class="table">
            <el-table-column
                    fixed
                    prop="img"
                    label="img"
                    width="100">
            </el-table-column>
            <el-table-column
                    prop="pid"
                    label="pid"
                    width="100">
            </el-table-column>
            <el-table-column
                    prop="name"
                    label="name"
                    width="300">
            </el-table-column>
            <el-table-column
                    prop="site_name"
                    label="site"
                    width="100">
            </el-table-column>
            <el-table-column
                    prop="query_click"
                    label="click"
                    width="100">
            </el-table-column>
            <el-table-column
                    prop="cate1"
                    label="cate1"
                    width="100">
            </el-table-column>
            <el-table-column
                    prop="cate2"
                    label="cate2"
                    width="100">
            </el-table-column>
            <el-table-column
                    prop="cate3"
                    label="cate3"
                    width="100">
            </el-table-column>
            <el-table-column
                    prop="clickct"
                    label="clickct"
                    width="100">
            </el-table-column>
            <el-table-column
                    prop="review_num"
                    label="review_num"
                    width="100">
            </el-table-column>
            <el-table-column
                    prop="review_rate"
                    label="review_rate"
                    width="100">
            </el-table-column>
        </el-table>
        <!--
        <el-pagination class="pagination" layout="prev, pager, next" :total="total" :page-size="pageSize"
                       v-on:current-change="changePage">
        </el-pagination>
        -->
        <db-modal :dialogFormVisible="dialogFormVisible" :form="form" v-on:canclemodal="dialogVisible"></db-modal>
    </div>
</template>

<script>
    import Bus from '../eventBus'
    import DbModal from './DbModal.vue'

    export default {
        data() {
            return {
                tableData: [],
                apiUrl: 'http://127.0.0.1:5000/api/v1/goods/10000397',
//                total: 0,
//                pageSize: 10,
//                currentPage: 1,
                pid: '',
                name: '',
                dialogFormVisible: false,
                form: '',
            }
        },
        components: {
            DbModal
        },

        mounted() {
            this.getGoods();
            Bus.$on('filterResultData', (data) => {
                this.tableData = data.results;
//                this.total = data.total_pages;
                this.pageSize = data.count;
                this.pid = data.pid;
                this.name = data.name;
                this.site_name = data.site_name;
                this.cate1 = data.cate1;
                this.cate2 = data.cate2;
                this.cate3 = data.cate3;
            });
        },

        methods: {
            dialogVisible: function () {
                this.dialogFormVisible = false;
            },

            getGoods: function () {
                this.$axios.get(this.apiUrl, {
//                    params: {
//                        page: this.currentPage,
//                        pid: this.pid,
//                        name: this.name
//                    }
                }).then((response) => {
                    this.tableData = response.data.results;
//                    this.total = response.data.total;
//                    this.pageSize = response.data.count;
                    console.log(response.data);
                }).catch(function (response) {
                    console.log(response)
                });
            },

            changePage: function (currentPage) {
//                this.currentPage = currentPage;
                this.getGoods()
            },

            editItem: function (index, rows) {
                this.dialogFormVisible = true;
                const itemId = rows[index].pid;
                const idurl = 'http://127.0.0.1:5000/api/v1/goods/' + itemId;
                this.$axios.get(idurl).then((response) => {
                    this.form = response.data;
                }).catch(function (response) {
                    console.log(response)
                });
            },
//            formatter(row, column) {
//                let data = this.$moment.unix(row.create_datetime);
//                return data.format('YYYY-MM-DD HH:mm:ss')
//            },
        }
    }
</script>

<style>
    .table {
        margin-top: 30px;
    }

    .pagination {
        margin-top: 10px;
        float: right;
    }
</style>