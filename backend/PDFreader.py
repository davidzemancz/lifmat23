from pypdf import PdfReader

def read_chapter(chap_num, pdf_name):
    reader = PdfReader(pdf_name)
    number_of_pages = len(reader.pages)
    text = ""
    chap_content = ""
    read = False
    for p in range(number_of_pages):
        text += reader.pages[p].extract_text()  

    for i in text.splitlines():
        t = i
        line = i.strip()
        if kapitoly[chap_num] in line.replace(" ", ""):
            read = True
        if len(kapitoly) > chap_num + 1 and kapitoly[chap_num + 1] in line.replace(" ", "") and read == True:
                read = False
        if read:
            if line != "":
                chap_content += line + "\n"
                print("##" + repr(t))
    return chap_content



reader = PdfReader("test_pdfs/omeprazol.pdf")
number_of_pages = len(reader.pages)
text = ""

for p in range(number_of_pages):
    text += reader.pages[p].extract_text()

kapitoly = [
    "1.NÁZEVPŘÍPRAVKU",
    "2.KVALITATIVNÍAKVANTITATIVNÍSLOŽENÍ",
    "3.LÉKOVÁFORMA",
    "4.KLINICKÉÚDAJE",
    "5.FARMAKOLOGICKÉVLASTNOSTI",
    "6.FARMACEUTICKÉÚDAJE",
    "7.DRŽITELROZHODNUTÍOREGISTRACI",
    "8.REGISTRAČNÍČÍSLO(A)",
    "9.DATUMPRVNÍREGISTRACE/PRODLOUŽENÍREGISTRACE",
    "10.DATUMREVIZETEXTU"
]


print(read_chapter(3,"test_pdfs/warfarin.pdf"))
#read_tables("test_pdfs/warfarin.pdf")