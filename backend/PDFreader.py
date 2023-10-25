from pypdf import PdfReader

def read_chapter(chap_num, pdf_names):
    #print(pdf_names)
    if len(pdf_names) > 2:
         return "Prosim o specifikaci"
    if chap_num < 0 or chap_num > 19:
         return ""
    
    chap_content = ""
    for p in pdf_names:
        pdf_path = f'../../lifmat23_data/spc/{p}'
        reader = PdfReader(pdf_path)
        number_of_pages = len(reader.pages)
        read = False
        text = "p\n"
        for p in range(number_of_pages):
            text += reader.pages[p].extract_text()  

        for i in text.splitlines():
            line = i.strip()
            #print(line.replace(" ", ""))
            if kapitoly[chap_num] in line.replace(" ", "").replace(".",""):
                read = True
            if len(kapitoly) > chap_num + 1 and kapitoly[chap_num + 1] in line.replace(" ", "").replace(".","") and read == True:
                    read = False
            if read:
                if line != "":
                    chap_content += line + "\n"
    #print(chap_content)
    return chap_content

kapitoly = [
    "1NÁZEVPŘÍPRAVKU",                                                             #0
    "2KVALITATIVNÍAKVANTITATIVNÍSLOŽENÍ",                                          #1
    "3LÉKOVÁFORMA",                                                                #2                                         
    "41Terapeutickéindikace",
    "42Dávkováníazpůsobpodání",
    "43Kontraindikace",
    "44Zvláštníupozorněníaopatřenípropoužití",
    "45Interakcesjinýmiléčivýmipřípravkyajinéformyinterakce",
    "46Fertilita,těhotenstvíakojení",
    "47Účinkynaschopnostříditaobsluhovatstroje",
    "48Nežádoucíúčinky",
    "49Předávkování",
    "51Farmakodynamickévlastnosti",
    "52Farmakokinetickévlastnosti",
    "53Předklinickéúdajevztahujícísekbezpečnosti",
    "6FARMACEUTICKÉÚDAJE",
    "7DRŽITELROZHODNUTÍOREGISTRACI",
    "8REGISTRAČNÍČÍSLO(A)",
    "9DATUMPRVNÍREGISTRACE/PRODLOUŽENÍREGISTRACE",
    "10DATUMREVIZETEXTU"
]

