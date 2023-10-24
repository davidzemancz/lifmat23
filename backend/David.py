import sqlite3
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def create_query(message):
    completion = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[
            {
                "role": "user", 
                "content": "Mám SQL VIEW 'leky' a v něm sloupce KOD_SUKL, NAZEV, SPC, SILA."
            },
             {
                "role": "user", 
                "content": f'Vytvoř query pro vrácení sloupce SPC podle sloucpů NAZEV a SILA.'
            },
            {
                "role": "user", 
                "content": f'Pro oba sloupce použij operátor LIKE s % a velká písmena.'
            },
            {
                "role": "user", 
                "content": f'Dotaz zní takto: {message}'
            },
            {
                "role": "user", 
                "content": "Vypiš pouze SQL query jako prostý text, ne jako kód, a nic dalšího."
            }
    ])
    return completion.choices[0].message.content

def get_pdfs(query):
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return list(dict.fromkeys([row[0] for row in rows if row[0] != '']))

def test():
    # question = 'Jaký je eliminační poločas warfarinu?'
    # question = 'Je pro člověka s horečkou lepší paralen grip nebo warfarin?'
    question = 'Jaká je doporučená dávka léku paralen grip 25mg?'
    # question = 'Lze použít omeprazol při diabetes?'
    # question = 'Je 1000mg léku atomoxetin actavis smrtelná dávka?'

    query = create_query(question)
    print(query)
    pdfs = get_pdfs(query)
    print(pdfs)
    print(len(pdfs))

test()
