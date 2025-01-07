'''
PROYECTOS DE HACKING ETICO WITH PYTHON
AUTOMATIZAR PENTESTING Y EXPLOTACION DE VULNERABILIDADES
'''

# Este proyecto demuestra cómo utilizar Python para automatizar el proceso de pentesting y exploitar vulnerabilidades, utilizando diversas bibliotecas como mmap y impacket.

import requests
from scapy.all import ARP, Ether, srp

# Función para escanear la red
def scan(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    return clients

# Ejemplo de escaneo
ip_range = "192.168.1.0/24"
clients = scan(ip_range)
for client in clients:
    print(f"IP: {client['ip']}, MAC: {client['mac']}")

# Comprobar si una URL es vulnerable
def check_vulnerability(url):
    response = requests.get(url)
    if "vulnerable" in response.text:
        print(f"{url} es vulnerable.")
    else:
        print(f"{url} no es vulnerable.")

# Uso de la función
check_vulnerability("http://example.com/vulnerable")