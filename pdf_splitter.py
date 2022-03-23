import sys
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf_half(path):

    file_name = os.path.splitext(os.path.basename(path))[0]
    
    pdf = PdfFileWriter(path)
    print(pdf.getNumpages)
    

if __name__ == "__main__":
    split_pdf_half(sys.argv[1])
