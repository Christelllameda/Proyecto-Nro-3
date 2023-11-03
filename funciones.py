import pandas as pd
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
#driver configuration
opciones=Options()
opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
opciones.add_experimental_option('useAutomationExtension', False)
opciones.headless=False    # si True, no aperece la ventana (headless=no visible)
opciones.add_argument('--start-maximized')         # comienza maximizado
#opciones.add_argument('user-data-dir=selenium')    # mantiene las cookies
#opciones.add_extension('driver_folder/adblock.crx')       # adblocker
opciones.add_argument('--incognito')

def obtener_datos_obra(url):
    
    driver = webdriver.Chrome(options = opciones)
    
    driver.get(url)
    
    # Encuentra los elementos relevantes en la página
    elementos = driver.find_elements(By.CSS_SELECTOR, 
                                     "#main-content > div > div > div.et_pb_section.et_pb_section_0_tb_body.et_section_regular")
    
    # Extrae y procesa los datos de la obra
    valencia = [elemento.text.split("\n") for elemento in elementos]
    obra = [item.split(": ", 1)[1] if ": " in item else item for item in valencia[0]]
    
    columnas = [item.split(":")[0] if ":" in item else item for item in valencia[0]]
    
    return obra



def crear_dataframe(obra, columnas):
    # Crea un DataFrame con los datos de la obra y las columnas proporcionadas
    df = pd.DataFrame([obra], columns=columnas)
    
    # Renombra las columnas según las especificaciones
    df = df.rename(columns={'LÍNEA 2 METRO DE VALENCIA': 'Obra', '47%': 'Ejecución física', 'S/I': 'Ejecución financiera'})
    
    return df