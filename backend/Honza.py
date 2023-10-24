import APIPrompt
import PDFreader
import openai

def get_answer(message, pdfs, chapters, context):
    text = ""
    cont = [x['text'] for x in  context]
    for c in chapters:
        text += PDFreader.read_chapter(c,pdfs)

    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {
          "role": "system", 
          "content": "Máš k dispozici následující kontext." + ",".join(cont)
        },
        {
          "role": "user",
          "content": "Na základě následující otázky najdi stručnou odpověď v následujícím textu. Otázka: " + message + " Text: " + text
        }
    ])

    return (response.choices[0].message.content)