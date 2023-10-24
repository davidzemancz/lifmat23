from flask import Flask, request
from flask_cors import CORS
from QueryCreator import create_query
import sqlite3
app = Flask(__name__)
CORS(app)

messages = []

def get_pdfs(query):
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return [row[0] for row in rows if row[0] != '']

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
    print(query)
    pdfs = get_pdfs(query)
    print(pdfs)

    # chaps = get_chapters(pdfs)
    # answer = ask(message, pdfs, chaps)
    
    # return {
    #     'isOutgoing': False,
    #     'text': answer
    # }

# Testy
get_answer('Jaká je doporučená dávka paralenu pro dospělého?')
get_answer('Na jaké indikace je abaktal určen?')
get_answer('Jaké má ewofex nežádoucí účinky?')
get_answer('Jaké jsou kontradikce má LUSIENNE?')

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

