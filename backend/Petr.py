import openai


def get_chapters(message):
    kapitoly_str = ",".join(kapitoly)
    res = respondPetr(message,kapitoly_str)
    l = res.split(",")
    for char in l:
        if len(char) > 2:
            return [3,4]

    if '3' not in l and "indikace" in message:
        l += [3] 

    if '10' not in l and "nezadouci ucinky" in message:
        l += [10]
    if '10' not in l and "nežádoucí" in message:
        l += [10]

    if '5' not in l and "kontraindikace" in message:
        l += [5]

    if '11' not in l and "predavkovani" in message:
        l += [11]
    if '10' not in l:
         l += [10]

    return list(map(int,l))

def response(question, kapitoly):
    return  openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
            {
                "role": "system", 
                "content": "Mám názvy kapitol v kterých jsou informace odpovídající názvu."
            },
             {
                "role": "user", 
                "content": f'Kterých všech z následujících kapitol se týká násleující dotaz. Dotaz:{question}, Kapitoly:{kapitoly}'
            },
            {
                "role": "assistant", 
                "content": "Vypiš index kapitol oddělěné čárkou, nic dalšího. Neumíš psát písmena. Indexy jsou od 0"
            }
    ])
     

def respondPetr(question, kapitoly):
    res =  response(question,kapitoly)
    return (res.choices[0].message.content)


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

