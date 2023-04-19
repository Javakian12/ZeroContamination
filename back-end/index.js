const app = require('express')();
const server = require('http').createServer(app);
const io = require('socket.io')(server);
io.on('connection', () => { console.log("Connected!") });
server.listen(19007);


io.on('uploadF', ()=> {

console.log("Recieved Image")


})