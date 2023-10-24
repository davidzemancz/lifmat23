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

  return response['choices'][0]['text']
  print(response['choices'][0]['text'])

prompt=PDFreader.read_chapter(2, "test_pdfs/warfarin.pdf")
# question="Jaká gramáž warfarinu je zmíněná v následujícím textu?"

chapters = []
doctor_prompt="Jaká je smrtelná dávka warfarinu."

for c in range(len(kapitoly)):
  question="Je " + kapitoly[c] + " Relevantni na dotaz: " + doctor_prompt + " ? Pouze ANO nebo NE"
  res = respond(question)
  if (res == "ANO"):
    chapters += [c]
  else:
    print(res)


print(chapters)