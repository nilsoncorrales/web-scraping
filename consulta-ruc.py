import pytesseract as tess
from PIL import Image

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import wget
from bs4 import BeautifulSoup
import requests
import urllib.request

# opciones de navegadcion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\Personal\\Downloads\\chromedriver_win32\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path, options=options)

# iniciar la pantalla
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

urlInit = 'https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/frameCriterioBusqueda.jsp'
driver.get(urlInit)

# obtenemos contenigo de pagina
page_source = driver.page_source

# leemos la data
soup = BeautifulSoup(page_source, 'lxml')
img = soup.img
src = img['src']

# descargamos imagen

# Set up the image URL
image_url = f"https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/{src}"

print(image_url)

# The following way works. Ref: https://stackoverflow.com/a/45358832/6064933
req = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
with open("captcha_image.jpg", "wb") as f:
    with urllib.request.urlopen(req) as r:
        f.write(r.read())

print('Image Successfully Downloaded: ')

tess.pytesseract.tesseract_cmd = r'D:\ProgramsFiles\Tesseract-OCR\tesseract.exe'
img = Image.open('captcha_image.jpg')
text = tess.image_to_string(img)

print(f'texto de la images es {text}')

time.sleep(3)

WebDriverWait(driver, 20)\
     .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > form > table > tbody > tr > td > table:nth-child(6) > tbody > tr:nth-child(2) > td:nth-child(6) > input[type=text]')))\
     .send_keys(text)




