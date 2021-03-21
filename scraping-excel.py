import pandas
import xlrd
import requests
from bs4 import BeautifulSoup


def extractLinkFromExcel():
    alLinks = []
    # Leemos el excel
    mainData_book = xlrd.open_workbook("DHL_ENERO_2021.xls", formatting_info=True)
    numSheets = mainData_book.nsheets
    sheetName = mainData_book.sheet_names()

    print('numero de hojas -> ', numSheets)
    print('nombre de hojas -> ', sheetName)

    sh = mainData_book.sheet_by_index(0)
    numRow = sh.nrows
    nameSheet = sh.name

    print("Cell D30 is -> {0}".format(sh.cell_value(rowx=1, colx=7)))

    for rx in range(1, sh.nrows):
        # leemos cada fila desde la columna 0 hasta la 8
        rowValues = sh.row_values(rx, start_colx=0, end_colx=8)
        # print("=====================================")
        # print(rowValues)
        link = sh.hyperlink_map.get((rx, 7))
        link = link.url_or_path
        alLinks.append(link)

    scrapingUlr(alLinks)


def scrapingUlr(alLinks):
    if len(alLinks) == 0:
        return
    linkScraping = alLinks.pop()
    r = requests.get(linkScraping)
    data = r.content.decode('utf-8', errors="replace")
    soup = BeautifulSoup(data, 'lxml')

    peruNews = soup.find_all('div', class_="col-xs-12 col-sm-8 col-md-9")
    container = peruNews[0]
    childs = container.div.contents
    objetExcel = []
    for child in childs:
        if child.name:
            head = child.strong.string
            body = child.span.string
            objetExcel.append({
                "head": head,
                "body": body
            })
    print(objetExcel)
    # return linkScraping
    return linkScraping


extractLinkFromExcel()
