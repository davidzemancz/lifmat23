import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def create_query(question):

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {
                "role": "user", 
                "content": "Mám SQL VIEW 'leky' a v něm sloupce KOD_SUKL a NAZEV."
            },
             {
                "role": "user", 
                "content": f'Vytvoř query pro vrácení všech KOD_SUKL pro následující dotaz: {question}'
            },
            {
                "role": "user", 
                "content": "Vypiš pouze SQL query a žádný text."
            }
    ])
    print(completion.choices[0].message.content)

create_query('Je lepší pro pacienta s rakovinou plic paralen nebo brufen? Má bolesti hlavy.')
