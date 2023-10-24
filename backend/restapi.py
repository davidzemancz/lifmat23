from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

messages = []

def create_query(message):
    return ''

def get_pdfs(query):
    return []

def get_chapters(message, pdfs):
    return []

def ask(message, pdfs, chapters):
    return ''

def get_answer(message):
    # Vygenerovat query do DN pro vraceni PDF
    # Nacist prislusna PDF ze souboru
    # Musim z PDF vybrat, ktery odstavec me zajima
    # Zeptam se na dotaz v kontextu prislusnych kapitol
    # Vratim odpoved
    query = create_query(message)
    pdfs = get_pdfs(query)
    chaps = get_chapters(pdfs)
    answer = ask(message, pdfs, chaps)
    
    return {
        'isOutgoing': False,
        'text': answer
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

