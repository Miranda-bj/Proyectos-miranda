'''
PROYECTOS DE HACKING ETICO WITH PYTHON
WEB SCRAPER Y ANALISIS DE INFORMACION
'''

# Un raspador web para obtener información de páginas web es muy útil y se
# puede realizar con requests y BeautifulSoup.

# PASOS
# Importa requests para realizar solicitudes HTTP y BeautifulSoup para el análisis.
# Define la función scrape_website que acepta una URL.
# Realiza una solicitud GET a la URL y crea un objeto BeautifulSoup.
# Extrae el título de la página y lo imprime.

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.text
    print(f"Title: {title}")

scrape_website("https://example.com")