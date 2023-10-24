import os
import openai
import PDFreader

openai.api_key = "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"


kapitoly = [
    "NÁZEV PŘÍPRAVKU",                                                             
    "KVALITATIVNÍ A KVANTITATIVN ÍSLOŽENÍ",                                          
    "LÉKOVÁ FORMA",                                                                                                       
    "Terapeutické indikace",
    "Dávkování a způsob podání",
    "Kontra indikace",
    "Zvláštní upozornění a opatření pro použití",
    "Interakce s jinými léčivými přípravky a jiné formy interakce",
    "Fertilita,těhotenství a kojení",
    "Účinky na schopnost řídit a obsluhovat stroje",
    "Nežádoucí účinky",
    "Předávkování",
    "Farmakodynamické vlastnosti",
    "Farmakokinetické vlastnosti",
    "Předklinické údaje vztahující se k bezpečnosti",
    "FARMACEUTICKÉ ÚDAJE",
    "DRŽITEL ROZHODNUTÍ O REGISTRACI",
    "REGISTRAČNÍ ČÍSLO(A)",
    "DATUM PRVNÍ REGISTRACE/PRODLOUŽENÍ REGISTRACE",
    "DATUM REVIZE TEXTU"
]

def respond(question):
  response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    # model="gpt-4-0613",
    prompt=question,
    max_tokens=50
  )

  print(response['choices'][0]['text'])

prompt=PDFreader.read_chapter(2, "test_pdfs/warfarin.pdf")
# question="Jaká gramáž warfarinu je zmíněná v následujícím textu?"

kapitoly_str=','.join(kapitoly)

doctor_prompt="Jaká je smrtelná dávka warfarinu."
question="Jakých kapitol z následujícího seznamu se týká tento text? Výsledek vrať jako pozice kapitol indexovaných od 0. Kapitoly: " + kapitoly_str + "Text: " + doctor_prompt

respond(question)