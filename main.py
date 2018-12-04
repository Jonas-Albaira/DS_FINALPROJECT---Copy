from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import os
#initialize Flask Application
app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )
#create global variables
users=[" "]*30
count = 0

#routing/mapping of pages, tie URL to a python function
#root of website
# @ symbolizes a decorator
@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")

def messageRecived():
  print( 'message was received!!!' )

#function for Multicasting Messages
@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )

@socketio.on( 'username' )
def receive_username(info):
    global count
    users[count]=info
    print(users)
    count+=1
    socketio.emit('display', users)
#make the app discoverable in the network
if __name__ == '__main__':
  socketio.run( app, host='0.0.0.0', debug=False )

