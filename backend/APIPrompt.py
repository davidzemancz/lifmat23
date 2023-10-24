import os
import openai
import PDFreader

openai.api_key = os.getenv("OPENAI_API_KEY")

def respond35(question):
  response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=question,
    max_tokens=100
  )

  return response['choices'][0]['text']

def respond4(question):
  response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": question}
    ])

  return (response['choices'][0]['message']['content'])

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

prompt = PDFreader.read_chapter(2, "test_pdfs/warfarin.pdf")

chapters = []
doctor_prompt = "Jaká je smrtelná dávka warfarinu."
doctor_prompt = "Jake jsou vedlejsi ucinky warfarinu pri brani s paralenem?"

areas = "Doporucena davka, Predavkovani, Inkompatibilita, Nezadouci ucinky."

kapitoly_str = ",".join(kapitoly)

question = "Jakých z následujícíh oblastí se týká následující dotaz? Můžeš vrátit víc oblastí. Oblasti: " + kapitoly_str + "Dotaz: " + doctor_prompt

print(respond4(question))
