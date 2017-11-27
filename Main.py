import os
import PyPDF2

dir = os.path.abspath(os.path.dirname(__file__)) + "/res/"


def parser(dir):
    for file in os.listdir(dir):
        extension = os.path.splitext(file)[-1].lower()
        if (extension == ".txt"):
            with open(dir + file, 'r+', encoding="utf8") as f:
                s = f.read()
                print(s)
        elif extension == ".pdf":
            p = PyPDF2.PdfFileReader(dir + file)
            if p.getDocumentInfo() is not None:
                print(p.getDocumentInfo())
                for page in range(0, p.getNumPages()):
                    if p.getPage(page) is not None:
                        print(p.getPage(page).extractText())
