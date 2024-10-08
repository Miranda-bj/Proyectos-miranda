# CODIGO HACKING ETICO PARA OBTENER LA CLAVE DEL WIFI
import subprocess

perfil_red = input("Introduce el nombre del perfil de red wifi: ")

try:
    
    resultados = subprocess.check_output(['netsh', 'wlan', 'show', 'profile',
                                        perfil_red], shell=True).decode('utf-8',
                                        errors='backslashreplace')
    
    # SI EL SISTEMA ES EN INGLES SE PONDRA 'KEY CONTENT'
    if 'contenido de la clave' in resultados:
        for line in resultados.split('\n'):
            if 'contenido de la clave' in line:
                password = line.split(':')[1].strip()
                print(f"la contraseña de la red {perfil_red} es: {password}")
                break
    else:
        print(f"no se pudo encontrar la contraseña para la red {perfil_red}")

except subprocess.CalledProcessError:
    print(f"no se pudo obtener la informacion del perfil {perfil_red}")
