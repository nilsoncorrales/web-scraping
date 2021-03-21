# libraries
import requests
from bs4 import BeautifulSoup
import json

karolGSongs = []


def extractLetter(dowloandLetter):
    if len(dowloandLetter) == 0:
        print('== FIN DE LA LISTA ==')
        print(json.dumps(karolGSongs, indent=1))
        return

    music = dowloandLetter.pop()
    name = music['title']
    song = music['href']

    r = requests.get(song)
    data = r.content.decode('utf-8', errors="replace")
    soup = BeautifulSoup(data, 'lxml')
    letter = soup.find_all('div', id="letra")
    content = letter[0].contents
    letter = ""
    for child in content:
        if child.name == 'p':
            childText = str(child).replace("</br>", " \n ")
            childText = childText.replace("<br/>", " \n ")
            childText = childText.replace("<p>", "")
            childText = childText.replace("</p>", "")
            letter += childText
    karolGSongs.append({
        "name": name,
        "song": letter
    })
    print(f'Descargando letra de cancion *{name}*')
    extractLetter(dowloandLetter)


def init():
    r = requests.get('https://servicios.noticiasperu.pe//gui/view/VistaPautaPrensa.php?idPauta=2101020140010025544&bool=1')
    data = r.content.decode('utf-8', errors="replace")
    soup = BeautifulSoup(data, 'lxml')
    print(soup)
    # obtengo el ul que contiene el nombre de la cancion y el url de a canción
    linksUl = soup.find_all('ul', class_="listado-letras")
    # me voy dentro del contenido de este arreglo
    content = linksUl[0].contents
    dowloandLetter = []
    for child in content:
        dowloandLetter.append({
            "title": child.a['title'],
            "href": f'https://www.musica.com/{child.a["href"]}'
        })
    print(dowloandLetter)
    extractLetter(dowloandLetter)


init()
