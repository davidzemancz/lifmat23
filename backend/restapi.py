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

def get_answer(message, pdfs, chapters, context):
    return Honza.get_answer(message, pdfs, chapters, context)


def vrat_context():
    if len(messages ) > 2:
        if 'chaps' in messages[-2]:
            return [x for x in messages[-3:-1]]
        return []
    return []


def ask(message):
    query = create_query(message)
    drugs = get_drugs(query)
    print(drugs)
    print(query)
    if len(drugs) > 10:
        return {
            'isOutgoing': False,
            'text': "Upřesněte prosím váš dotaz nebo specifikujte přesné jméno léku."
    }
    elif len(drugs) > 2:
        return {
            'isOutgoing': False,
            'text': 'Vyberte prosím lék, který vás zajímá.',
            'options':[{'name': drug[2], 'file': drug[1] } for drug in drugs],
            'pastId':len(messages) - 1
        }
    elif len(drugs) == 0:  
        context = vrat_context()
        drugs = [('0209947',)] # Docasna oprava
        if len(context) > 0:
            chaps = list(dict.fromkeys(get_chapters(message) + context[1]['chaps']))
            pdfs_list = context[1]['pdf_list']
            answer = get_answer(message, pdfs_list, chaps, context)

            return {
                'isOutgoing': False,
                'text': answer,
                'refs': [{ 'url': f'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/{drug[0]}', 'info': f'kapitoly {",".join([str(c) for c in chaps])}'} for drug in drugs],
                'chaps': chaps,
                'pdf_list': pdfs_list
            }

        return {
            'isOutgoing': False,
            'text': "K vašemu dotazu nebyly nalezeny žádné informace."

    }
    else: 
        chaps = get_chapters(message)
        if len(chaps) > 0: 
            pdfs_list = list(map(lambda x: x[1], drugs))
            context = ""
            answer = get_answer(message, pdfs_list, chaps, context)

            return {
                'isOutgoing': False,
                'text': answer,
                'refs': [{ 'url': f'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/{drug[0]}', 'info': f'kapitoly {",".join([str(c) for c in chaps])}'} for drug in drugs],
                'chaps': chaps,
                'pdf_list': pdfs_list
            }
        else:
            return {
                'isOutgoing': False,
                'text': "K vašemu dotazu nebyly nalezeny žádné informace."
            }

def ask_detailed(file, pastId):
    prev_message = messages[pastId]
    
    chaps = get_chapters(prev_message['text'])
    if len(chaps) > 0:
        pdfs_list = [file]
        answer_text = get_answer(prev_message['text'], pdfs_list, chaps, [])
        return {
            'isOutgoing': False,
            'text': answer_text,
            'refs': [ {'url': f'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/{file}', 'info': f'kapitoly {",".join([str(c) for c in chaps])}'}],
            'chaps': chaps,
            'pdf_list': pdfs_list
        }
    else:
        return {
            'isOutgoing': False,
            'text': "Nenalezeny žádné kapitoly."
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

    debug = False
    if debug:
        time.sleep(3)
        answer = get_mock_answer()
        messages.append(answer)
        return {}

    if 'file' in message:
        file = message['file']
        pastId = int(message['pastId'])
        print(file, pastId)
        answer = ask_detailed(file, pastId)
        messages.append(answer)

    else:
        # time.sleep(3)
        # answer = get_mock_answer()
        answer = ask(message['text'])
        messages.append(answer)

    return {}

def get_mock_answer():
    return {
            'text': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Duis condimentum augue id magna semper rutrum. Aenean fermentum risus id tortor. Integer lacinia. Nullam rhoncus aliquam metus. Integer imperdiet lectus quis justo. ',
            'isOutgoing': False,
            'pastId': 1,
            'refs':[
                {
                    'url': 'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/0094156',
                    'info': "kapitoly 4,5",
                    
                },
                {
                    'url': 'https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/0255111',
                    'info': "kapitoly 6",
                }
            ],
            'options': [{
                'name': 'PARALEN GRIP HORKÝ NÁPOJ ECHINACEA A ŠÍPKY 500MG/10MG', 
                'file': 'SPC194750.pdf'
                }, ]
        } 

