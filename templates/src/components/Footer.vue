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

    a {
        text-decoration: none;
    }

    .footer-main {
        font-size: 0;
        padding-top: 40px;
        display: inline-block;
    }

    .footer-main .footer-main-title {
        line-height: 1;
        font-size: 22px;
        margin: 0;
    }

    .footer-main .footer-main-link {
        display: inline-block;
        margin: 12px 18px 0 0;
        line-height: 1;
        font-size: 12px;
        color: #768193;
    }

    .layout-copy .footdoc {
        display: inline-block;
        text-align: center;
        color: #8d99ab;
        width: 570px;
        vertical-align: middle;
        font-size: 12px;
    }
</style>