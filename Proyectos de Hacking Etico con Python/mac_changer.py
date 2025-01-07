'''
PROYECTOS DE HACKING ETICO WITH PYTHON
MAC CHANGER
'''

# El siguiente código permite cambiar la dirección MAC de una interfaz de red utilizando la biblioteca subprocess.

# PASOS
# Importa la biblioteca subprocess para ejecutar comandos del sistema.
# Define la función change_mac que toma dos parámetros: la interfaz de red y la nueva dirección MAC.
# Usa subprocess.call para ejecutar comandos del sistema que cambian la dirección MAC.
# Llama a la función con una interfaz específica y una nueva dirección MAC.

import subprocess

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

change_mac("eth0", "00:11:22:33:44:55")