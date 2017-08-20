<template>
    <div class="container">
        <div class="footer-main">
            <p class="footer-main-title">{{ message }}</p>
            <a href="https://github.com/Seolhun" target="_blank" class="footer-main-link">Github</a>
            <a href="mailto:shun10114@gmail.com" class="footer-main-link">Email</a>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                message: 'Hun, Seol',
            }
        },
    }
</script>

<style scoped>
    .container {
        width: auto;
        padding: 0px 30px;
        text-align: right;
    }

    .footer-main{
        padding : 10px 0px;
    }

    .footer-main .footer-main-title {
        line-height: 1;
        font-size: 22px;
    }

    .footer-main .footer-main-link {
        display: inline-block;
        margin: 12px 0px 0 0;
        line-height: 1;
        font-size: 12px;
        color: #768193;
    }
</style>