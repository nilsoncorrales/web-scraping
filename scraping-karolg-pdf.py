import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

karolGSongs = []


def init():
    r = requests.get('https://www.letras.com/karol-g/')
    data = r.content.decode('utf-8', errors="replace")
    soup = BeautifulSoup(data, 'lxml')
    # obtengo el ul que contiene el nombre de la cancion y el url de a canción
    listMusic = soup.find_all('ol', class_="cnt-list cnt-list--num -flex-col-2 js-song-list")
    # me voy dentro del contenido de este arreglo
    content = listMusic[0].contents
    dowloandLetter = []
    for child in content:
        if child != ' ':
            dowloandLetter.append({
                "title": child['data-name'],
                "url": child['data-shareurl']
            })
    extractLetter(dowloandLetter)
    generatePdf()


def extractLetter(dowloandLetter):
    if len(dowloandLetter) == 0:
        print('== FIN DE LA LISTA ==')
        print(karolGSongs)
        return

    music = dowloandLetter.pop()
    name = music['title']
    song = music['url']

    r = requests.get(song)
    data = r.content.decode('utf-8', errors="replace")
    soup = BeautifulSoup(data, 'lxml')
    letter = soup.find_all('div', class_="cnt-letra p402_premium")
    content = letter[0].contents
    letterCustom = ""
    for child in content:
        if child.name == 'p':
            childText = str(child).replace("</br>", " \n ")
            childText = childText.replace("<br/>", " \n ")
            childText = childText.replace("<p>", "")
            childText = childText.replace("</p>", "")
            letterCustom += (childText + " \n ")
    karolGSongs.append({
        "name": name,
        "letter": letterCustom
    })
    print(f'Descargando letra de cancion *{name}*')
    extractLetter(dowloandLetter)


def generatePdf():
    pdf = FPDF()
    for value in karolGSongs:
        data = value['letter']
        data = data.encode('latin-1', 'replace').decode('latin-1')
        pdf.add_page()
        pdf.set_font("Helvetica", size=16)
        pdf.cell(200, 10, txt=value['name'], ln=1, align="C")
        data = str(data).split("\n")
        for item in data:
            pdf.set_font("Helvetica", size=10)
            pdf.cell(200, 10, txt=item, ln=1, align="C")
            pdf.ln(1)
    pdf.output("simple_demo.pdf")





init()

