import sqlite3
import QueryCreator
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def create_query(message):
    completion = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[
            {
                "role": "user", 
                "content": "Mám SQL VIEW 'leky' a v něm sloupce KOD_SUKL a NAZEV a SPC."
            },
             {
                "role": "user", 
                "content": f'Vytvoř query pro vrácení sloupce SPC podle názvu léku psaného velkými písmeny pro následující dotaz: {message}'
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
    return [row[0] for row in rows if row[0] != '']