import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf_half(path):
    with open(path, 'rb') as file:
        pdf = PdfFileReader(file)
        num_of_pages = pdf.getNumPages()
        print(num_of_pages)
    

if __name__ == "__main__":
    split_pdf_half(sys.argv[1])
