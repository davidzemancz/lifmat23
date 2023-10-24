from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

messages = []

def get_answer(message):
    # Vygenerovat query do DN pro vraceni PDF
    # Nacist prislusna PDF ze souboru
    # Musim z PDF vybrat, ktery odstavec me zajima
    # Zeptam se na dotaz v kontextu prislusnych kapitol
    # Vratim odpoved

    return {
        'isOutgoing': False,
        'text': 'nema slov'
    }

@app.route('/delete-messages')
def delete_messages():
    global messages
    messages = []
    return {}

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
    answer = get_answer(message)
    
    messages.append(message)
    messages.append(answer)

    return {}

