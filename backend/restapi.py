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

    if len(pdfs) > 2:
        return {
        'isOutgoing': False,
        'text': "Zadejte přesnější dotaz."
    }
    elif len(pdfs) == 0:  
        return {
        'isOutgoing': False,
        'text': "Nenalezeny žádné pdf."
    }
    else: chaps = get_chapters(message)
        
    if len(chaps) > 0: 
        answer = get_answer(message, pdfs, chaps)
    else:
        return {
        'isOutgoing': False,
        'text': "Nenalezeny žádné kapitoly."
    }

    return {
        'isOutgoing': False,
        'text': answer
    }

# Testy
#print(ask('Jaká je doporučená dávka paralenu pro dospělého?'))
#print(ask('Na jaké indikace je paralen určen?'))
#print(ask('Jaké má ewofex nežádoucí účinky?'))
# print(ask('Jaké jsou kontradikce má LUSIENNE?'))

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
        'text': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Duis condimentum augue id magna semper rutrum. Aenean fermentum risus id tortor. Integer lacinia. Nullam rhoncus aliquam metus. Integer imperdiet lectus quis justo. ',
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

