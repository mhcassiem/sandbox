import pikepdf
from pikepdf._core import Pdf


class PDFPWD:
    def __init__(self, pdf_loc, pdf_pwd, pdf_save_loc, pdf_save):
        self.pdf_loc = pdf_loc
        self.pdf_pwd = pdf_pwd
        self.pdf_save = pdf_save if pdf_save else pdf_loc.split('/')[-1]
        self.pdf_save_loc = pdf_save_loc if pdf_save_loc else "/".join(pdf_loc.split('/')[:-1])

    def open_pdf(self):
        print("\nProcessing...\n")
        try:
            return pikepdf.open(self.pdf_loc, password=self.pdf_pwd)
        except Exception as e:
            print(f'Exception in opening PDF:\n{e}')

    def save_pdf(self, pdf: Pdf):
        try:
            pdf.save(f'{self.pdf_save_loc}/{self.pdf_save}')
            print("The password successfully removed from the PDF")
            print(f"\aLocation: {self.pdf_save_loc}/{self.pdf_save}")
        except Exception as e:
            print(f'Exception in saving PDF:\n{e}')
