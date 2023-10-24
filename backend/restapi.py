from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

messages = []

@app.route('/messages')
def get_messages():
    global messages

    return {
        'messages': messages
    }

@app.route('/post-message', methods=['POST'])
def post_message():
    global messages
    
    message = request.json
    messages.append(message)
    return {}