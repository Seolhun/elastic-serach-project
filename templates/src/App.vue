<template>
    <div class="wrapper">
        <bz-header>

        </bz-header>

        <el-row class="container">
            <el-col :span="4" class="menu">
                <bz-sidebar></bz-sidebar>
            </el-col>
            <el-col :span="20" class="content">
                <bz-filter></bz-filter>
                <bz-table></bz-table>

            </el-col>
        </el-row>

        <el-row>
            <el-col :span="24">
                <footer class="footer">
                    <bz-footer>

                    </bz-footer>
                </footer>
            </el-col>
        </el-row>


    </div>
</template>
<script>
    import BzHeader from './components/BzHeader.vue'
    import BzSidebar from './components/BzSidebar.vue'
    import BzFilter from './components/BzFilter.vue'
    import BzTable from './components/BzTable.vue'
    import BzFooter from './components/BzFooter.vue'
    import ElRow from "element-ui/packages/row/src/row";

    export default {
        name: 'app',
        components: {
            ElRow,
            BzHeader,
            BzSidebar,
            BzFilter,
            BzTable,
            BzFooter
        },
    }

</script>

<style>
    body {
        font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", Arial, sans-serif;
        margin: 0;
        display: flex;
        min-height: 100vh;
        flex-direction: column;
    }

    .wrapper {

        position: relative;
    }

    footer, div {
        display: block;
    }

    .container {
        padding-top: 70px;
        flex: 1;
    }

    .container, .wrapper {
        height: 100%;
    }

    .menu {
        height: 100%;
        background-color: #ffffff;
    }

    .content {
        padding-top: 25px;
        padding-right: 25px;
        padding-bottom: 125px;
        padding-left: 25px;
    }

    .footer {
        height: 120px;
        background-color: #ffc620;
        color: #ffffff;
        width: 100%;
        z-index: 1000;
        margin-top: -120px;
        line-height: 1;
        font-size: 22px;
    }

    .search-text {
        width: 30%;
    }
</style>