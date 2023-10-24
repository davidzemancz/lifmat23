import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def create_query(question):

    completion = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[
            {
                "role": "user", 
                "content": "Mám SQL VIEW 'leky' a v něm sloupce KOD_SUKL a NAZEV a SPC."
            },
             {
                "role": "user", 
                "content": f'Vytvoř query pro vrácení sloupce SPC podle názvu léku psaného velkými písmeny pro následující dotaz: {question}'
            },
            {
                "role": "user", 
                "content": "Vypiš pouze SQL query jako prostý text, ne jako kód, a nic dalšího."
            }
    ])
    return completion.choices[0].message.content

# answer = create_query('Je lepší pro pacienta s rakovinou plic paralen nebo brufen? Má bolesti hlavy.')
# print(answer)
