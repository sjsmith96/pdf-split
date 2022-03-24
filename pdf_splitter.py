import sys
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def create_split_pdf(page_start, page_end, original_pdf, file_name):
    write = PdfFileWriter()
    for i in range(page_start, page_end):
        write.addPage(original_pdf.getPage(i))
    split = open(f'{file_name}.pdf', 'wb')
    write.write(split)

def split_pdf_half(path):

    file_name = os.path.splitext(os.path.basename(path))[0]
    
    pdf = PdfFileReader(path)
    num_of_pages = pdf.getNumPages()

    create_split_pdf(0, int(num_of_pages / 2), pdf, f'{file_name}_p1')
    create_split_pdf(int(num_of_pages / 2), num_of_pages, pdf, f'{file_name}_p2')

if __name__ == "__main__":
    split_pdf_half(sys.argv[1])
