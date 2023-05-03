const express = require('express')
const socketIo = require('socket.io')
const http = require('http')
const { exec } = require('node:child_process')
const PORT = process.env.PORT || 8080
const cors = require ('cors');
const server = http.createServer(app)
const fs = require('fs');
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

  socket.on("uploadF", ({file, name}, callback)=> { //send to python via socketIO
    console.log("Recieved Image, sending to python...");

    try {
      fs.writeFileSync(`../yolov7/inference/images/${name}`, file);
    } catch (err) {
      console.error(err)
    }
    //perform learning
    exec(`cd .. && cd yolov7 && python detect.py --weights runs/train/zerowaste-lr0_0001-ep100/weights/best.pt --conf 0.25 --save-txt --img-size 640 --source inference/images/${name}`, (err, output) => { 
      // once the command has completed, the callback function is called
      if (err) {
          // log and return if we encounter an error
          console.error("could not execute command: ", err)
          return
      }
      
      // log the output received from the command
      console.log("Output: \n", output)
      fs.readFile(`../yolov7/runs/detect/exp/${name}`, function read(err, data) {
        if (err) {
          throw err;
        }
        const content = data;

        fs.readFile(`../yolov7/runs/detect/exp/${name}`, function read(err, dataCoord) {
          if (err) {
            throw err;
          }
          const contentCoord = dataCoord;
        })

        //delete folder where learned image was stored (save space)
        exec(`cd .. && cd yolov7/runs/detect && rmdir /s /q exp && cd .. && cd .. && cd inference/images && del ${name}`, (err, output) => { //if server is running on linux, change this command (rmdir and del)
          // once the command has completed, the callback function is called
          if (err) {
              // log and return if we encounter an error
              console.error("could not execute command: ", err)
              return
          }
          else{
            console.log("Removed directory and file")
          } 
        });
        callback({
          file: content
        })
      
  })
});

});
});

setInterval(()=>{
     io.to(`clock-room`).emit('time', new Date())
},1000)
server.listen(PORT, err=> {
  if(err) console.log(err)
  console.log(`Server running on Port `, PORT)
})