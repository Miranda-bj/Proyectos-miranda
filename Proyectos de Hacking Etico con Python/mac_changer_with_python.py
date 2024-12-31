'''
PROYECTOS DE HACKING ETICO WITH PYTHON
MAC CHANGER
'''
# Este proyecto implica cambiar la dirección MAC de una interfaz de red usando Python.

# Descripción: Se utiliza la librería subprocess para ejecutar comandos de sistema que cambian la dirección MAC.

import subprocess

# Leer la dirección MAC actual
def get_mac_address(interface):
    result = subprocess.run(["ip", "link", "show", interface], capture_output=True)
    return result.stdout.decode().split("link/ether")[-1].strip().split()

# Cambiar la dirección MAC
def change_mac_address(interface, new_mac):
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])

# Ejemplo de uso
interface = "eth0"
new_mac = "00:11:22:33:44:55"
current_mac = get_mac_address(interface)
print(f"Dirección MAC actual: {current_mac}")
change_mac_address(interface, new_mac)