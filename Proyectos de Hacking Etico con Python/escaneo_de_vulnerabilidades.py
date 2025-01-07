'''
PROYECTOS DE HACKING ETICO WITH PYTHON
ESCANEO DE VULNERABILIDADES
'''

# Este proyecto implica utilizar herramientas como OWASP ZAP para escanear vulnerabilidades en páginas web

# Se muestra cómo identificar vulnerabilidades utilizando Python y herramientas de terceros.

import requests

# Función para escanear vulnerabilidades
def scan_vulnerabilities(url):
    response = requests.get(url)
    if "vulnerable" in response.text:
        print(f'Se encontró una vulnerabilidad en {url}')
    else:
        print(f'No se encontró vulnerabilidad en {url}')

# Ejemplo de uso
url_to_scan = "http://example.com"
scan_vulnerabilities(url_to_scan)