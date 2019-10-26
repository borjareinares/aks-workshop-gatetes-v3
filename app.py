from flask import Flask, render_template
import os
import random
import socket

app = Flask(__name__)

@app.route('/')
def index():
    pod_ip = os.getenv('POD_IP')

    return render_template('index.html', pod_ip=pod_ip)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
