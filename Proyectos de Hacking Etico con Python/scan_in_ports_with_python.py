'''
PROYECTOS DE HACKING ETICO WITH PYTHON
ESCANEO DE PUERTOS
'''
# Este proyecto implica escanear puertos abiertos en un servidor o dispositivo.

# Descripción: Utiliza la librería socket o scapy para escanear puertos y determinar si están abiertos o cerrados

import socket

# Función para escanear puertos
def scan_ports(target):
    open_ports = []
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Ejemplo de uso
target_ip = "192.168.1.1"
open_ports = scan_ports(target_ip)
print(f"Puertos abiertos en {target_ip}: {open_ports}")