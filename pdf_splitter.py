import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

if __name__ == "__main__":
    print(f'Argument count: {len(sys.argv)}')
    for arg in sys.argv:
        print(f'Argument: {arg}')
