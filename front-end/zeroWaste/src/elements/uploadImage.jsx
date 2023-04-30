import React, { useState, useEffect } from "react";
import {Box, Button, Typography, Grid} from "@mui/material"
import {io} from 'socket.io-client'
import App from "../../App";

const UploadAndDisplayImage = ({}) => {

  const [selectedImage, setSelectedImage] = useState(null);
  const mainState = useState(Object)
  const [unused, setState, stateRf] = mainState
  const io = require("socket.io-client");

    useEffect(()=>{
        setState(p=>({...p,...{
            image: selectedImage,
        }}))
    },[selectedImage])

    const submitItem=()=>{
      socket.emit("uploadF", selectedImage, (status) => {
           console.log(status);
        }); 
     console.log("fire")
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
            <Button sx={{bgcolor:"#3aa0bf", color:"#ffffff"}} onClick={()=>submitItem()}>Submit for Classification</Button>
          <img
            alt="not found"
            width={"250px"}
            src={URL.createObjectURL(selectedImage)}
          />
          <br />
          <button onClick={() => setSelectedImage(null)}>Remove</button>
          </Box>
      )}
        {stateRf?.current?.submit}
      <br />
      
      <input
        type="file"
        name="myImage"
        onChange={(event) => {
          console.log(event.target.files[0]);
          setSelectedImage(event.target.files[0]);
        }}
      />
      
    </Box>
    
    </Grid>
  );
};

export default UploadAndDisplayImage;