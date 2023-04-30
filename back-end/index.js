const app = require('express')();
const server = require('http').createServer(app);
const io = require('socket.io')(server);
io.on('connection', () => { console.log("Connected!") });
server.listen(8080);

console.log("Fire")

io.on('uploadF', ()=> {

console.log("Recieved Image")


})

//segmantic segmentation