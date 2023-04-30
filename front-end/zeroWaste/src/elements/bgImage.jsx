
import React, { useEffect } from 'react';
import { Text, View, TextInput, ImageBackground, StyleSheet, Dimensions } from 'react-native';
import { Typography, Box, Button, TextField } from '@mui/material';
import useState from 'react-usestateref'
import ImageUpload from './uploadImage';

const screenHeight = Dimensions.get('window').height;
  const screenWidth = Dimensions.get('window').width

  const BackgroundImg = ({socket}) => {
    const mainState = useState(Object)
    const [unused, setState, stateRf] = mainState

    const openFade=()=>{
        console.log(name)
        setState(p=>({...p,...{
            imageUpload: <ImageUpload socket={socket} ImageName={name}/>,
        }})) 
    }

    useEffect(()=>{
        
    },[])

    useEffect(()=>{
        setState(p=>({...p,...{
            uploadScreen: <View>
            <ImageBackground
              source={{
                uri: 
      'https://media3.giphy.com/media/ITRemFlr5tS39AzQUL/giphy.gif?cid=ecf05e477yqty41vkgk3d8c2ymwxfu0xtitagnpwzdmqhfkb&rid=giphy.gif&ct=g',
              }}
              resizeMode="stretch"
              style={styles.img}>
                
                    {stateRf?.current?.imageUpload ? stateRf?.current?.imageUpload : <Box sx={{alignItems: 'center',justifyContent: 'center'}}>
                <Button sx={{background: 'red', boxShadow:'3'}} onClick={()=>openFade()}>
              <Typography sx={{color: 'black', borderWidth:'10px'}}>
                Upload File
              </Typography>
              </Button> </Box>
              }
            </ImageBackground>
          </View>
        }}))
    },[stateRf?.current?.imageUpload])


    return ( <Box>
      {stateRf?.current?.uploadScreen}
      </Box>
      );
  };

export default BackgroundImg;
  
const styles = StyleSheet.create({
  img: {
    height: screenHeight,
    width: screenWidth,
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: '-999',
  },
  input: {
    height: 40,
    margin: 12,
    borderWidth: 2,
    padding: 10,
  },
});