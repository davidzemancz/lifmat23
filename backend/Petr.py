import openai


def get_chapters(message):
    kapitoly_str = ",".join(kapitoly)
    res = respondPetr(message,kapitoly_str)
    print(res)
    return list(map(int,res.split(",")))

def respondPetr(question, kapitoly):
  response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
            {
                "role": "system", 
                "content": "Mám názvy kapitol v kterých jsou informace odpovídající názvu."
            },
             {
                "role": "user", 
                "content": f'Kterých z následujících kapitol se dotaz týká násleující dotaz. Dotaz:{question}, Kapitoly:{kapitoly}'
            },
            {
                "role": "assistant", 
                "content": "Vypiš indexy čísla kapitol oddělěné čárkou, nic dalšího. Neumíš psát písmena. Indexy jsou od 0"
            }
    ])

  return (response.choices[0].message.content)


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

