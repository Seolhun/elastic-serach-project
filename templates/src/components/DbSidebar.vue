<template>
    <li class="el-menu-item is-active" style="">{{msg}}</li>
</template>

<script>

    export default {
        name: 'db-sidebar',
        data() {
            return {
                msg: 'Searching'
            }
        }
    }

</script>

<style>
    li {
        padding-left: 20px;
    }
</style>
