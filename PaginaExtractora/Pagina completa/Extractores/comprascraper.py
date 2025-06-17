from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time

# Configurar Selenium con opciones recomendadas
options = Options()
options.add_argument("--headless") 
options.add_argument("--disable-gpu") 
options.add_argument("--no-sandbox")  
options.add_argument("--disable-software-rasterizer") 
options.add_argument("--disable-dev-shm-usage") 
options.add_argument("--window-size=1920,1080")  

# Iniciar el navegador con las opciones
driver = webdriver.Chrome(options=options)


# URL de CompraGamer
url = "https://www.compragamer.com/index.php?seccion=1&categoria=3&nro_max=40"
driver.get(url)
time.sleep(5)

productos = []

# Buscar productos
items = driver.find_elements(By.CLASS_NAME, "producto")

for item in items:
    try:
        nombre = item.find_element(By.CLASS_NAME, "nombre_producto").text
        precio = item.find_element(By.CLASS_NAME, "precio").text
        img = item.find_element(By.TAG_NAME, "img").get_attribute("src")
        
        productos.append({
            "nombre": nombre,
            "precio": precio,
            "imagen": img
        })
    except Exception as e:
        print("Error procesando producto:", e)

driver.quit()

# Guardar en JSON
with open("Datos/productos.json", "w", encoding="utf-8") as f:
    json.dump(productos, f, ensure_ascii=False, indent=4)
