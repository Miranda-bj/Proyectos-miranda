'''
PROYECTOS DE HACKING ETICO WITH PYTHON
IDENTIFICAR USUARIOS CONECTADOS A LA RED
'''

# Este proyecto implica crear un script que identifique a los usuarios conectados a una red local.

# Utilizando la biblioteca scapy, el código realiza un escaneo de la red y obtiene información sobre los dispositivos conectados.

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

# Ejemplo de uso
ip_range = "192.168.1.0/24"
clients = scan(ip_range)
for client in clients:
    print(f"IP: {client['ip']}, MAC: {client['mac']}")