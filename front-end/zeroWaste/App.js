import { StatusBar } from 'expo-status-bar';
import React, { useEffect } from 'react';
import {io} from 'socket.io-client'
import { Text, View, TextInput, ImageBackground, StyleSheet, Dimensions } from 'react-native';
import BackgroundImg from './src/elements/bgImage';
import useState from 'react-usestateref'
import { Typography, Box } from '@mui/material';
import { RecoilRoot } from 'recoil';


export default function App() {
  const mainState = useState(Object)
  const [unused, setState, stateRf] = mainState 
  //const [isConnected, setIsConnected] = useState(socket.connected);
  const [fooEvents, setFooEvents] = useState([]);

  useEffect(()=>{
    console.log(stateRf?.current?.submit)
  },[stateRf?.current?.submit])

  return (
    <View style={styles.container}>
      <RecoilRoot>
      <Box sx={{backgroundColor: "", width: '100%', display:"flex", justifyContent:"center", alignItems:"center"}}>
      <Typography sx={{fontSize:'2.5rem'}}>
      Recycling Classifier & Cardboard Contamination Detection
      </Typography>
      </Box>
      <StatusBar style="auto" />
      {stateRf?.current?.submit}
      <BackgroundImg />
      </RecoilRoot>
    </View>
  );
}

const topText = StyleSheet.create({
  container: {
    backgroundColor: '#cccc00',
  },
})
const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'start',
  },
});
