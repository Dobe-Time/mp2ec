from flask import Flask
from flask import request
import stress
import socket
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        subprocess.Popen("python", "stress.py")
        return socket.gethostname() 
    else:
        return socket.gethostname() 


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80, debug = True)
