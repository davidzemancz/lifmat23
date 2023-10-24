import yake
from pypdf import PdfReader

def extract_word(text):
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(text)

    for kw in keywords:
	    print(kw)

def test_pdf():
    pdf_path = "test_pdfs/omep_ot.pdf"
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    text = ""
    for p in range(number_of_pages):
        text += reader.pages[p].extract_text()  
    extract_word(text) 


test_pdf()