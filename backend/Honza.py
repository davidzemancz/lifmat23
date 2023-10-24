import APIPrompt
import PDFreader

def get_answer(message, pdfs, chapters):
    text = ""
    for c in chapters:
        text += PDFreader.read_chapter(c,pdfs[0])
    
    prompt = "Na základě následující otázky najdi odpověď v následujícím textu. Odpověz stručně. Otázka: " + message + "Text : " + text
    res = APIPrompt.respond4(prompt)
    return res