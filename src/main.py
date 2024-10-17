import os
from dotenv import load_dotenv, dotenv_values 
# load environment variables
load_dotenv() 

from utils import api, database
from controllers import question

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, debug=True, cors_allowed_origins='*')

# define flask routes
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/questions/common', methods=['GET'])
def commonQuestions():
    return question.getCommonHandler()

# define socket events
@socketio.on('chat')
def chatHandler(receive):
    print(receive)

if __name__ == '__main__':
    app.run(debug=True)
