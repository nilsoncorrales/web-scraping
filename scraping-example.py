#libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd


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

driver.get('https://www.eltiempo.es/')

locator = 'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.')

WebDriverWait(driver, 20)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator))).click()


WebDriverWait(driver, 20)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#inputSearch')))\
    .send_keys('lima peru')


WebDriverWait(driver, 20)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.icon.icon-search'))).click()

locator2 = 'i.icon_weather_s.flag-icon.flag-icon-pe.flag-icon-squared'
WebDriverWait(driver, 20)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator2))).click()

WebDriverWait(driver, 20)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/main/div[4]/div/section[3]/section/div/article/section/ul/li[2]/a'))).click()


WebDriverWait(driver, 20)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/main/div[4]/div/section[3]/section/div[1]/ul')))


texto_columna = driver.find_element_by_xpath('/html/body/div[7]/main/div[4]/div/section[3]/section/div[1]/ul')

texto_columna = texto_columna.text

tiempo_hoy = texto_columna.split('Mañana')[0].split('\n')[1: -1]


horas = list()
temp = list()
v_viento = list()
for i in range(0, len(tiempo_hoy), 4):
    horas.append(tiempo_hoy[i])
    temp.append(tiempo_hoy[i+1])
    v_viento.append(tiempo_hoy[i+2])

df = pd.readjs({'Horas': horas, 'Temperatura': temp, 'Velocidad de viento x hora': v_viento})
print(df)
df.to_csv('tiempo_hoy.csv', index=False)





