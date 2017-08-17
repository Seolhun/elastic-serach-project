<template>
    <div>
        <el-table
                :data="tableData"
                border
                style="width: 100%"
                class="table">
            <el-table-column
                    fixed
                    prop="pid"
                    label="pid"
                    width="200">
            </el-table-column>
            <el-table-column
                    prop="img"
                    label="img"
                    width="300">
            </el-table-column>
            <el-table-column
                    prop="name"
                    label="name"
                    width="500">
            </el-table-column>
        </el-table>
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
                apiUrl: 'http://127.0.0.1:9200/goods/_search',
                pid: '',
                img: '',
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
                console.log("data", data);
                this.tableData = data.results;
                this.pid = data.pid;
                this.img = data.img;
                this.name = data.name;
            });
        },

        methods: {
            dialogVisible: function () {
                this.dialogFormVisible = false;
            },
            getGoods: function () {
                this.$axios.get(this.apiUrl, {
                    params: {
                        pid: this.pid,
                        img: this.img,
                        name: this.name
                    }
                }).then((response) => {
                    this.tableData = response.data.results;
                    console.log(response.data);
                }).catch(function (response) {
                    console.log(response)
                });
            },
            changePage: function (currentPage) {
                this.currentPage = currentPage;
                this.getGoods()
            },
            editItem: function (index, rows) {
                this.dialogFormVisible = true;
                const pid = rows[index].pid;
                const idurl = 'http://127.0.0.1:9200/goods/_search';
                this.$axios.get(idurl).then((response) => {
                    this.form = response.data;
                }).catch(function (response) {
                    console.log(response)
                });
            },
            formatter(row, column) {
                let data = this.$moment.unix(row.create_datetime);
                return data.format('YYYY-MM-DD HH:mm:ss')
            },
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