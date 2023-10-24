import os
import openai
import PDFreader

openai.api_key = os.getenv("OPENAI_API_KEY")

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
    prompt=question,
    max_tokens=50
  )

  print(response['choices'][0]['text'])

prompt=PDFreader.read_chapter(2, "test_pdfs/warfarin.pdf")
question="Jaká gramáž warfarinu je zmíněná v následujícím textu?"

# prompt="From the following text, find how many tables of paralen should I take: Paralen is medical drug. You should take 1-2 tablets of paralen. Never take more than 5 tablets."

respond(question+prompt)

