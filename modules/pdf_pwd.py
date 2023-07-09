import pikepdf
from pikepdf._core import Pdf

pdf_loc = input("PDF location: ")
pdf_pass = input("PDF password: ")

pdf = pikepdf.open(pdf_loc, password=pdf_pass)

print("\nProcessing...\n")

pdf_save = input("Save file as: ")
pdf_loc2 = input("Save location: ")

pdf.save(pdf_loc2 + '\\' + pdf_save)

print("The password successfully removed from the PDF")
print("\aLocation: " + pdf_loc + '\\' + pdf_save)


class PDFPWD:
    def __init__(self, pdf_loc, pdf_pwd, pdf_save_loc, pdf_save):
        self.pdf_loc = pdf_loc
        self.pdf_pwd = pdf_pwd
        self.pdf_save = pdf_save
        self.pdf_save_loc = pdf_save_loc if pdf_save_loc else pdf_loc

    def open_pdf(self):
        try:
            return pikepdf.open(self.pdf_loc, password=self.pdf_pwd)
        except Exception as e:
            print(f'Exception in opening PDF:\n{e}')

    def save_pdf(self, pdf: Pdf):
        try:
            pdf.save(f'{self.pdf_save_loc}\\{pdf_save}')
        except Exception as e:
            print(f'Exception in saving PDF:\n{e}')
