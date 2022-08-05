import webbrowser
import fpdf
import requests


def generate_pdf():
    pdf = fpdf.FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0.01, 10, 'nombre: ' + data['name'])
    pdf.cell(0.01, 20, 'tipo: ' + data['animal_type'])
    pdf.cell(0.01, 30, 'habitat: ' + data['habitat'])
    pdf.cell(0.01, 40, 'alimento: ' + data['diet'])
    pdf.output('animal.pdf')


def open_tabs():
    url = data["image_link"]
    webbrowser.open_new('./animal.pdf')
    webbrowser.open(url)


response = requests.get('https://zoo-animal-api.herokuapp.com/animals/rand')
data = response.json()

generate_pdf()
open_tabs()
