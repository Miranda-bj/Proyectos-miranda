'''
PROYECTOS DE HACKING ETICO WITH PYTHON
ESCANEO DE PUERTOS Y DETECCION DE VULNERBILIDADES
'''

# Este proyecto consiste en crear un escáner de puertos y detectar vulnerabilidades utilizando Python y Nmap.

#  El curso detalla cómo instalar las herramientas, escribir el script en Python, y cómo interpretar los resultados.

import nmap

# Inicializar el escáner
nm = nmap.PortScanner()

# Función para escanear un host específico
def scan_host(ip):
    nm.scan(ip, '1-1024')  # Escanear puertos del 1 al 1024
    for proto in nm[ip].all_protocols():
        print(f'Protocolo : {proto}')
        lport = nm[ip][proto].keys()
        for port in sorted(lport):
            print(f'Puerto : {port}\tEstado : {nm[ip][proto][port]["state"]}')

# Ejemplo de uso
ip_to_scan = '192.168.1.1'
scan_host(ip_to_scan)