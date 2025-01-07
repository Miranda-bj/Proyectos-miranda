'''
PROYECTOS DE HACKING ETICO WITH PYTHON
ESCANEO DE PUERTOS Y ANALISIS DE INFORMACION DE PAGINAS WEB
'''

# En este proyecto, se muestra cómo realizar un escaneo de puertos y analizar la información de las páginas web usando Python. Utiliza la librería requests para obtener datos a través de HTTP/HTTPS.

import socket
import requests

# Función para escanear puertos
def scan_ports(target):
    open_ports = []
    for port in range(1, 1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Análisis de información a través de HTTP
def analyze_website(url):
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {response.headers}")

# Realizar escaneo de puertos
target_ip = "192.168.1.1"
print(f"Escaneando puertos en {target_ip}...")
open_ports = scan_ports(target_ip)
print(f"Puertos abiertos: {open_ports}")

# Análisis de una página web
analyze_website("http://example.com")