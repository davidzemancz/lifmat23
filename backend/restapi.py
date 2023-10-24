from flask import Flask, request
from flask_cors import CORS
import David
import Honza
import Petr
import time

app = Flask(__name__)
CORS(app)

messages = []

def create_query(message):
    return David.create_query(message)

def get_pdfs(query):
    return David.get_pdfs(query)

def get_chapters(message):
    return Petr.get_chapters(message)

def get_answer(message, pdfs, chapters):
    return Honza.get_answer(message, pdfs, chapters)

def ask(message):
  
    query = create_query(message)
    pdfs = get_pdfs(query)
    chaps = get_chapters(message)
    answer = get_answer(message, pdfs, chaps)

    return {
        'isOutgoing': False,
        'text': answer
    }

# Testy
# print(ask('Jaká je doporučená dávka paralenu pro dospělého?'))
#get_answer('Na jaké indikace je paralen určen?')
#get_answer('Jaké má ewofex nežádoucí účinky?')
# get_answer('Jaké jsou kontradikce má LUSIENNE?')

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
    messages.append(message)

    time.sleep(5)

    answer = {
        'text': 'posli nudes',
        'isOutgoing': False,
        'refs':[
            {
                'url': 'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/0094156',
                'info': "kapitoly 4,5"
            },
             {
                'url': 'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/0255111',
                'info': "kapitoly 6"
            }
        ]
     } # ask(message['text'])
    messages.append(answer)

    return {}

