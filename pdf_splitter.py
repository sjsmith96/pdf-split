import sys
import os
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter

def create_split_pdf(page_start, page_end, original_pdf, file_name):
    write = PdfFileWriter()
    for i in range(page_start, page_end):
        write.addPage(original_pdf.getPage(i))
    split = open(f'{file_name}.pdf', 'wb')
    write.write(split)
    split.close()

def split_pdf(path, num_of_splits):
    file_name = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path, strict = False)
    num_of_pages = pdf.getNumPages()

    pages_per_split = int(num_of_pages / num_of_splits)
    create_split_pdf(0, pages_per_split + (num_of_pages % num_of_splits), pdf, f'{file_name}_p1')
    for i in range(1, num_of_splits):
        page_start = (i * pages_per_split) + (num_of_pages % num_of_splits)
        page_end = page_start + pages_per_split
        create_split_pdf(page_start, page_end, pdf, f'{file_name}_p{i + 1}')
    
if __name__ == "__main__":
    # Using a library to parse command line arguments lol
    parser = argparse.ArgumentParser(description="Splits PDF files evenly(ish)")
    parser.add_argument('path', type=str, help='Path to the pdf to be split. (required)')
    parser.add_argument('splits', type=int, nargs='?', default=2, help='Number of times to split. Defaults to 2. (optional)')
    args = parser.parse_args()
    split_pdf(args.path, args.splits)
