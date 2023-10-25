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
            #print(line.replace(" ", ""))
            if kapitoly[chap_num] in line.replace(" ", ""):
                read = True
            if len(kapitoly) > chap_num + 1 and kapitoly[chap_num + 1] in line.replace(" ", "") and read == True:
                    read = False
            if read:
                if line != "":
                    chap_content += line + "\n"
    #print(chap_content)
    return chap_content

kapitoly = [
    "1.NÁZEVPŘÍPRAVKU",                                                             #0
    "2.KVALITATIVNÍAKVANTITATIVNÍSLOŽENÍ",                                          #1
    "3.LÉKOVÁFORMA",                                                                #2                                         
    "4.1.Terapeutickéindikace",
    "4.2.Dávkováníazpůsobpodání",
    "4.3.Kontraindikace",
    "4.4.Zvláštníupozorněníaopatřenípropoužití",
    "4.5.Interakcesjinýmiléčivýmipřípravkyajinéformyinterakce",
    "4.6.Fertilita,těhotenstvíakojení",
    "4.7.Účinkynaschopnostříditaobsluhovatstroje",
    "4.8.Nežádoucíúčinky",
    "4.9.Předávkování",
    "5.1.Farmakodynamickévlastnosti",
    "5.2.Farmakokinetickévlastnosti",
    "5.3.Předklinickéúdajevztahujícísekbezpečnosti",
    "6.FARMACEUTICKÉÚDAJE",
    "7.DRŽITELROZHODNUTÍOREGISTRACI",
    "8.REGISTRAČNÍČÍSLO(A)",
    "9.DATUMPRVNÍREGISTRACE/PRODLOUŽENÍREGISTRACE",
    "10.DATUMREVIZETEXTU"
]

pdf = "SPC198710.pdf"
print(read_chapter(4,[pdf]))

