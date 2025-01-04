'''
PROYECTOS DE HACKING ETICO WITH PYTHON
EXPLOTACION DE VULNERABILIDADES
'''

# Explotación de Vulnerabilidades:
# Utiliza bibliotecas como impacket para ejecutar exploits sobre los objetivos detectados

from impacket import smb

# Ejemplo de conexión SMB
smb_connection = smb.SMBConnection('192.168.1.5', '192.168.1.6')
smb_connection.login('username', 'password')
print(smb_connection.listShares())