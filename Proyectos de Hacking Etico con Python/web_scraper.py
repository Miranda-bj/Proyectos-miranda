'''
PROYECTOS DE HACKING ETICO WITH PYTHON
WEB SCRAPER
'''

# Este proyecto implica crear un scraper web utilizando requests y BeautifulSoup.

# Explicación Paso a Paso
# Se hace una solicitud HTTP para obtener el contenido de la página.
# Se parsea el contenido HTML para extraer información específica.

import requests
from bs4 import BeautifulSoup

# Función para extraer información de una página web
def web_scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for title in soup.find_all('h1'):
        print(title.text)

# Ejemplo de uso
web_scraper('https://example.com')