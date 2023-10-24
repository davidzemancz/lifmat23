import os
import openai
import PDFreader

openai.api_key = "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"
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

def respond35(question):
  response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    # model="gpt-4-0613",
    prompt=question,
    max_tokens=50
  )

  return response['choices'][0]['text']
  print(response['choices'][0]['text'])

def respond4(question):
  response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": question}
    ])

  return (response['choices'][0]['message']['content'])

prompt=PDFreader.read_chapter(2, "test_pdfs/warfarin.pdf")

chapters = []
doctor_prompt="Jaká je smrtelná dávka warfarinu."

for c in range(len(kapitoly)):
  question="Je " + kapitoly[c] + " Relevantni na dotaz: " + doctor_prompt + " ? Odpověz pouze ANO nebo NE"
  if ("ANO" in respond4(question).upper()):
    chapters += [c]

print(chapters)

