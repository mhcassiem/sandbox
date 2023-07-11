import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

from modules.pdf_pwd import PDFPWD

app = typer.Typer()


@app.command('pdf_pwd')
def remove_pdf_pwd():
    rprint("[yellow]=============================================[yello]")
    rprint("[green bold]PDF location: :[green bold]")
    pdf_loc = input()
    rprint("[green bold]PDF password: :[green bold]")
    pdf_pass = input()
    rprint("[green bold]Save PDF as (keep blank to use original name): :[green bold]")
    pdf_save = input()
    rprint("[green bold]Enter PDF save location :[green bold]")
    pdf_save_loc = input()
    pdf_pwd = PDFPWD(pdf_loc, pdf_pass, pdf_save_loc, pdf_save)
    pdf = pdf_pwd.open_pdf()
    pdf_pwd.save_pdf(pdf)


@app.command("hello")
def sample_func():
    rprint("[red bold]Hello[/red bold] [yellow]World[yello]")


if __name__ == "__main__":
    app()
