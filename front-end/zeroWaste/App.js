import { StatusBar } from 'expo-status-bar';
import React, { useEffect } from 'react';
import {io} from 'socket.io-client'
import { Text, View, TextInput, ImageBackground, StyleSheet, Dimensions } from 'react-native';
import BackgroundImg from './src/elements/bgImage';
import useState from 'react-usestateref'
import { Typography, Box } from '@mui/material';


export default function App() {
  const mainState = useState(Object)
  const [unused, setState, stateRf] = mainState 
  //const [isConnected, setIsConnected] = useState(socket.connected);
  const [fooEvents, setFooEvents] = useState([]);
  const [time, setTime] = useState('fetching')  
  useEffect(()=>{
    const socket = io('http://localhost:8080')
    socket.on('connect', ()=>console.log(socket.id))
    socket.on('connect_error', ()=>{
      setTimeout(()=>socket.connect(),5000)
    })
   socket.on('time', (data)=>setTime(data))
   socket.on('disconnect',()=>setTime('server disconnected'))
 },[])

  useEffect(()=>{
    console.log(stateRf?.current?.submit)
  },[stateRf?.current?.submit])

  return (
    <View style={styles.container}>
      <Box sx={{backgroundColor: "", width: '100%', display:"flex", justifyContent:"center", alignItems:"center"}}>
      <Typography sx={{fontSize:'2.5rem'}}>
      Recycling Classifier & Cardboard Contamination Detection
      </Typography>
      </Box>
      <StatusBar style="auto" />
      {stateRf?.current?.submit}
      <BackgroundImg socket={socket}/>
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
