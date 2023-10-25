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
                "content": "Write me just a drug names from following prompt without quotes separated by comma. If there is no drug names, write text NOTHING"
            },
             {
                "role": "user", 
                "content": f'{message}'
            },
            # {
            #     "role": "user", 
            #     "content": f'Použij klíčové slovo LIKE. Vlož "%" mezi všechna slova. Dále použij UPPER.'
            # },
            # {
            #     "role": "user", 
            #     "content": f'Dotaz zní takto: {message}'
            # },
            #  {
            #     "role": "user", 
            #     "content": f'Pokud dotaz neobsahuje název léku, vrať query, která nevrátí žádná data.'
            # },
            # {
            #     "role": "user", 
            #     "content": "Vypiš pouze SQL query jako prostý text, ne jako kód, a nic dalšího."
            # }
    ])
    drug_names =  completion.choices[0].message.content

    return 'SELECT NAZEV, KOD_SUKL, SPC FROM leky WHERE ' + " OR ".join(["UPPER(NAZEV) LIKE '%" + drug_name.upper().replace(" ", "%") + "%'" for drug_name in drug_names.split(",")])

def get_drugs(query):
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    print(query)
    cur.execute(query)
    rows = cur.fetchall()
    pdfs = {}
    for row in rows:
        if len(row) > 2 and row[2] != '':
            pdfs[row[2]] = (row[0], row[1])
    return [(pdfs[pdf][1], pdf, pdfs[pdf][0]) for pdf in pdfs]

def test():
    question = 'Na jaké indikace je určen MAGNEROT 500MG?'
    # question = 'Je pro člověka s horečkou lepší paralen rapid 500mg nebo warfarin pmcs 2mg?'
    # question = 'Jaká je doporučená dávka léku paralen grip 25mg?'
    # question = 'Lze použít lék omeprazol při diabetes?'
    # question = 'Je dávka 1000mg léku atomoxetin actavis smrtelná dávka?'

    query = create_query(question)
    print(query)
    pdfs = get_drugs(query)
    print(pdfs)
    print(query)
    print(len(pdfs))

# test()
