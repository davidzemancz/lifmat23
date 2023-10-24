from pypdf import PdfReader



def read_chapter(chap_num, pdf_names):
    #print(pdf_names)
    if len(pdf_names) > 2:
         return "Prosim o specifikaci"
    chap_content = ""
    for p in pdf_names:
        pdf_path = f'../../lifmat23_data/spc/{p}'
        reader = PdfReader(pdf_path)
        number_of_pages = len(reader.pages)
        read = False
        text = ""
        for p in range(number_of_pages):
            text += reader.pages[p].extract_text()  

        for i in text.splitlines():
            line = i.strip()
            if kapitoly[chap_num] in line.replace(" ", ""):
                read = True
            if len(kapitoly) > chap_num + 1 and kapitoly[chap_num + 1] in line.replace(" ", "") and read == True:
                    read = False
            if read:
                if line != "":
                    chap_content += line + "\n"
    print(chap_content)
    return chap_content

kapitoly = [
    "1.NÁZEVPŘÍPRAVKU",                                                             #0
    "2.KVALITATIVNÍAKVANTITATIVNÍSLOŽENÍ",                                          #1
    "3.LÉKOVÁFORMA",                                                                #2                                         
    "4.1Terapeutickéindikace",
    "4.2Dávkováníazpůsobpodání",
    "4.3Kontraindikace",
    "4.4Zvláštníupozorněníaopatřenípropoužití",
    "4.5Interakcesjinýmiléčivýmipřípravkyajinéformyinterakce",
    "4.6Fertilita,těhotenstvíakojení",
    "4.7Účinkynaschopnostříditaobsluhovatstroje",
    "4.8Nežádoucíúčinky",
    "4.9Předávkování",
    "5.1Farmakodynamickévlastnosti",
    "5.2Farmakokinetickévlastnosti",
    "5.3Předklinickéúdajevztahujícísekbezpečnosti",
    "6.FARMACEUTICKÉÚDAJE",
    "7.DRŽITELROZHODNUTÍOREGISTRACI",
    "8.REGISTRAČNÍČÍSLO(A)",
    "9.DATUMPRVNÍREGISTRACE/PRODLOUŽENÍREGISTRACE",
    "10.DATUMREVIZETEXTU"
]
