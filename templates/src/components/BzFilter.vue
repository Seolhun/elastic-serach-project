<template>
    <div class="search-div">
        <el-form :inline="true" :model="formInline">
            <el-form-item label="Category">
                <el-select v-model="formInline.cate1" clearable placeholder="select cate1"
                           v-on:visible-change="selectDemo">
                    <el-option
                            v-for="item in type_options"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
                <el-select v-model="formInline.cate2" clearable placeholder="select cate2"
                           v-on:visible-change="selectDemo">
                    <el-option
                            v-for="item in type_options"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
                <el-select v-model="formInline.cate3" clearable placeholder="select cate3"
                           v-on:visible-change="selectDemo">
                    <el-option
                            v-for="item in type_options"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>

            <div>
                <el-input type="warning" style="width: 70%"></el-input>
                <el-button :plain="true" type="warning">Search</el-button>
            </div>

        </el-form>
    </div>
</template>

<script>
    import lodash from 'lodash'
    import Bus from '../eventBus'
    import ElInput from "../../node_modules/element-ui/packages/input/src/input.vue";

    export default {
        components: {ElInput},
        name: 'bz-filter',
        data() {
            return {
                type_options: [],
                formInline: {
                    cate1: '',
                    cate2: '',
                    cate3: ''
                },
                formLabelWidth: '120px'
            }
        },

        watch: {
            'formInline.sex': 'filterResultData',
            'formInline.email': 'filterResultData'
        },
        methods: {
            selectDemo: function (params) {
                if (params) {
                    this.$axios.get("http://127.0.0.1:5000/api/persons/sex")
                        .then((response) => {
                            this.type_options = response.data;
                            console.log(response.data);
                        }).catch(function (response) {
                        console.log(response)
                    });
                }

            },
            filterResultData: _.debounce(
                function () {
                    this.$axios.get("http://127.0.0.1:5000/api/persons", {
                        params: {
                            sex: this.formInline.sex,
                            email: this.formInline.email,
                        }
                    }).then((response) => {
                        response.data['sex'] = this.formInline.sex;
                        response.data['email'] = this.formInline.email;
                        Bus.$emit('filterResultData', response.data);
                        console.log(response.data);
                    }).catch(function (response) {
                        console.log(response)
                    });

                },
                500
            ),
        }
    }
</script>
<style>
    .search-div {
        text-align: center;
    }

</style>