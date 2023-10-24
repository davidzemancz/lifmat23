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

def get_drugs(query):
    return David.get_drugs(query)

def get_chapters(message):
    return Petr.get_chapters(message)

def get_answer(message, pdfs, chapters):
    return Honza.get_answer(message, pdfs, chapters)

def ask(message):
    query = create_query(message)
    drugs = get_drugs(query)
    if len(drugs) > 10:
        return {
            'isOutgoing': False,
            'text': "Upřesněte prosím váš dotaz nebo specifikujte přesné jméno léku."
    }
    elif len(drugs) > 2:
        return {
            'isOutgoing': False,
            'text': 'Vyberte prosím lék, který vás zajímá.',
            'options':[{'name': drug[2], 'url': f'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/{drug[0]}' } for drug in drugs]
        }
    elif len(drugs) == 0:  
        return {
            'isOutgoing': False,
            'text': "K vašemu dotazu nebyly nalezeny žádné informace."
    }
    else: 
        chaps = get_chapters(message)
        
    if len(chaps) > 0: 
        pdfs_list = list(map(lambda x: x[1], drugs))
        answer = get_answer(message, pdfs_list, chaps)
    else:
        return {
        'isOutgoing': False,
        'text': "Nenalezeny žádné kapitoly."
    }

    return {
        'isOutgoing': False,
        'text': answer,
        'refs': [{ 'url': f'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/{drug[0]}', 'info': f'kapitoly {",".join([str(c) for c in chaps])}'} for drug in drugs]
    }

# Testy
# print(ask('Na jaké indikace je určen MAGNEROT 500MG?'))
# print(ask('Na jaké indikace je paralen grip určen?'))
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

    time.sleep(3)
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
        ],
        'options': [{'name': 'PARALEN GRIP HORKÝ NÁPOJ ECHINACEA A ŠÍPKY 500MG/10MG', 'url': 'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/0230361'}, {'name': 'PARALEN GRIP CHŘIPKA A BOLEST 500MG/25MG/5MG', 'url': 'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/0254428'}, {'name': 'PARALEN GRIP CHŘIPKA A KAŠEL 500MG/15MG/5MG', 'url': 'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/0254464'}, {'name': 'PARALEN GRIP HORKÝ NÁPOJ CITRÓN 650MG/10MG', 'url': 'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/0254468'}, {'name': 'PARALEN GRIP HORKÝ NÁPOJ NEO 500MG/10MG', 'url': 'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/0254470'}, {'name': 'PARALEN GRIP HORKÝ NÁPOJ POMERANČ A ZÁZVOR 500MG/10MG', 'url': 'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/0254472'}, {'name': 'PARALEN GRIP HORKÝ NÁPOJ ECHINACEA A ŠÍPKY 500MG/10MG', 'url': 'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/0258170'}]
     } 
    # answer = ask(message['text'])
    messages.append(answer)

    return {}

