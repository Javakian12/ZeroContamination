import React, { useState, useEffect } from "react";
import {Box, Button, Typography, Grid} from "@mui/material"
import { useRecoilState } from "recoil";
import {io} from 'socket.io-client'
import App from "../../App";
import * as globalState from "../../globalState"

const UploadAndDisplayImage = ({}) => {

  const [selectedImage, setSelectedImage] = useState(null);
  const mainState = useState(Object)
  const [unused, setState, stateRf] = mainState
  const io = require("socket.io-client");
  const [time, setTime] = useState('fetching') 
  const [appSocket, setAppSocket] = useRecoilState(globalState.appSocketState) 
  const allowedFileTypes = ["image/png", "image/jpeg"]

  var socketIO = appSocket.get('socketIO')
  
  useEffect(()=>{
    if(!appSocket.has('socketIO')) { console.log("Attempting to connect to socketIO") }
    setAppSocket(p=>{p.set('socketIO',io('http://localhost:8080')); return new Map (p)})
 },[!appSocket.has('socketIO')])

 useEffect(()=>{
  if(appSocket.has('socketIO')) { console.log("Connected status of socketIO:", appSocket.get('socketIO')?.connected) }
},[appSocket])

    useEffect(()=>{
        setState(p=>({...p,...{
            image: selectedImage,
        }}))
    },[selectedImage])

    const submitItem=()=>{
      socketIO.emit("uploadF", {file: selectedImage, name: selectedImage?.name ? selectedImage?.name : "test1000"}, (response) => { 
          var data = new Blob([response?.file], {type: allowedFileTypes});
          var jpgURL = window.URL.createObjectURL(data);
          var tempLink = document.createElement('a');
          tempLink.href = jpgURL;
          tempLink.setAttribute('download', 'classification.jpg');
          tempLink.click();
        }); 
        setState(p=>({...p,...{
            submit: <Box bgcolor='red' width='100%'><Typography>Submitted file, waiting for response...</Typography></Box>
        }}))
    }

  return (
    <Grid item sm={6}>
    <Box bgcolor='grey' borderRadius='10px' padding='3%' alignItems='center' display="inline-grid" justifyContent="flex-end" sx={{textAlignLast:'center'}}>
      <Typography bgcolor='red' sx={{padding:'2%',borderRadius:'10px', boxShadow:'3'}}>Upload Image for Recycling Detection and Cardboard Contamination Segmenter</Typography>

      {selectedImage && (
        <Box padding='2%' justifyContent="center" display='flex' sx={{gap:'1%'}}>
            <Button sx={{bgcolor:"#3aa0bf", color:"#ffffff", boxShadow:'3'}} onClick={()=>submitItem()}>Submit for Classification</Button>
          <img
            alt="not found"
            width={"250px"}
            src={URL.createObjectURL(selectedImage)}
          />
          <br />
          <Button sx={{boxShadow:'3', bgcolor: 'white'}} onClick={() => setSelectedImage(null)}>Remove</Button>
          </Box>
      )}
      <br />
      
      <input
        type="file"
        name="myImage"
        onChange={(event) => {
          console.log(event.target.files[0]);
          setSelectedImage(event.target.files[0]);
        }}
      />
      {stateRf?.current?.submit}
      
    </Box>
    
    </Grid>
  );
};

export default UploadAndDisplayImage;