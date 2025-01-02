'''
PROYECTOS DE HACKING ETICO WITH PYTHON
CAMBIAR DIRECCION MAC
'''

# Este proyecto implica crear un script en Python para cambiar la dirección MAC de una interfaz de red. Aquí se explica paso a paso cómo hacerlo:

# Se utiliza la biblioteca subprocess para ejecutar comandos del sistema.

# El código permite leer la dirección MAC actual, solicitar una nueva dirección MAC al usuario y ejecutar los comandos necesarios para realizar el cambio.

import subprocess

# Leer la dirección MAC actual
def get_mac_address(interface):
    result = subprocess.run(["ip", "link", "show", interface], capture_output=True)
    return result.stdout.decode().split("link/ether")[-1].strip()

# Cambiar la dirección MAC
def change_mac_address(interface, new_mac):
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])

# Ejemplo de uso
interface = "eth0"
new_mac = input("Introduce la nueva dirección MAC: ")
current_mac = get_mac_address(interface)
print(f"Dirección MAC actual: {current_mac}")
change_mac_address(interface, new_mac)
print(f"Dirección MAC cambiada a: {new_mac}")