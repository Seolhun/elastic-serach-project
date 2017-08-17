/**
 * Created by gubaoer on 17/5/10.
 */


var path = require('path');
module.exports = {
    dev: {
        outputPath: path.resolve(__dirname, '../dist'),
        outputPublicPath: '/',
        port: 9000
    },
    prod: {
        outputPath: path.resolve(__dirname, '../dist'),
        outputPublicPath: '/'
    }
}