from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketIO = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketIO.on('message')
def handle_message(msg):
    print(msg)
    socketIO.emit('message', msg)

    if __name__ == "__main__":
        socketIO.run( app , debug = True)