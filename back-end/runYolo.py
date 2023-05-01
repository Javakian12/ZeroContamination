import socketio

sio = socketio.Client(reconnection=True, reconnection_attempts=float('inf'))

sio.connect('http://localhost:8080',transports="websocket")

@sio.event
def connect():
    print('connection established')

@sio.on("learnReq")
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.wait()