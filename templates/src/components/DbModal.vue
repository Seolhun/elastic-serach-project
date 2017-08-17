<template>
    <el-dialog title="Edit" v-model="dialogFormVisible" :close-on-click-modal="false" :show-close="false">
        <el-form :model="form">
            <el-form-item label="pid" :label-width="formLabelWidth">
                <el-input :disabled="true" v-model="form.pid" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="img" :label-width="formLabelWidth">
                <el-input :disabled="true" v-model="form.img" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="name" :label-width="formLabelWidth">
                <el-input :disabled="true" v-model="form.name" auto-complete="off"></el-input>
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button :plain="true" type="danger" v-on:click="canclemodal">Cancel</el-button>
            <el-button :plain="true" @click="updateForm(form)">Save</el-button>
        </div>
    </el-dialog>
</template>


<script>
    export default {
        data() {
            return {
                formLabelWidth: '120px',
            }
        },
        props: ['dialogFormVisible', 'form'],

        methods: {
            updateForm: function (formName) {
                let pid = formName.pid;
                let img = formName.img;
                let name = formName.name;
                this.$axios.put('http://127.0.0.1:9200/goods/_search', {
                    pid: pid,
                    img: img,
                    name: name
                })
                    .then(function (response) {
                        console.log(response);
                        this.form = response.data;
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
                location.reload();
            },
            canclemodal: function () {
                this.$emit('canclemodal');
            }
        }

    }

</script>