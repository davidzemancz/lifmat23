from flask import Flask, request
from flask_cors import CORS
from QueryCreator import create_query
import sqlite3
import APIPrompt
import PDFreader
app = Flask(__name__)
CORS(app)

messages = []

def get_pdfs(query):
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return [row[0] for row in rows if row[0] != '']

def get_chapters(message):
    prompt = "Jakých z následujícíh oblastí se týká následující dotaz? Můžeš vrátit víc oblastí. Vrať výsledek jako indexy odělené čárkou. Oblasti: " + APIPrompt.kapitoly_str + "Dotaz: " + message
    res = APIPrompt.respond4(prompt)
    return  list(map(int,res.split(",")))

def ask(message, pdfs, chapters):
    text = ""
    for c in chapters:
        text += PDFreader.read_chapter(c,pdfs[0])
    
    print(text)
    return text
    return read_chapter()

def get_answer(message):
    # Vygenerovat query do DN pro vraceni PDF
    # Nacist prislusna PDF ze souboru
    # Musim z PDF vybrat, ktery odstavec me zajima
    # Zeptam se na dotaz v kontextu prislusnych kapitol
    # Vratim odpoved
    query = create_query(message)
    pdfs = get_pdfs(query)
    chaps = get_chapters(message)
    print(chaps)
    answer = ask(message, pdfs, chaps)
    
    return {
        'isOutgoing': False,
        'text': answer
    }

# Testy
get_answer('Jaká je doporučená dávka paralenu pro dospělého?')
# get_answer('Na jaké indikace je abaktal určen?')
# get_answer('Jaké má ewofex nežádoucí účinky?')
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
    answer = get_answer(message)
    
    messages.append(message)
    messages.append(answer)

    return {}

