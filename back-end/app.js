const express = require('express')
const socketIo = require('socket.io')
const http = require('http')
const PORT = process.env.PORT || 8080
const cors = require ('cors');
const server = http.createServer(app)
const io = socketIo(server,{ 
    cors: {
      origin: 'http://localhost:8080'
    }
}) //in case server and client run on different urls
var app = express();

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});
io.on('connection',(socket)=>{
  console.log(`client connected: `,socket.id)
  
  socket.join('clock-room')
  
  socket.on('disconnect',(reason)=>{
    console.log(reason)
  })

  io.on('uploadF', ()=> {

    console.log("Recieved Image")
    
    
    })





})
setInterval(()=>{
     io.to(`clock-room`).emit('time', new Date())
},1000)
server.listen(PORT, err=> {
  if(err) console.log(err)
  console.log(`Server running on Port `, PORT)
})