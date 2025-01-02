'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN ALGORITMO DE ENCRIPTACION
'''

# Crea un sistema que permita encriptar y desencriptar texto utilizando un algoritmo simple (Cifrado César).

# PASOS
# Paso 1: Define una clase CifradoCesar que contenga métodos para encriptar y desencriptar.
# Paso 2: Implementa la lógica del cifrado y el descifrado.
# Paso 3: Proporciona un método para recibir texto y la clave de encriptación.
# Paso 4: Agrega una interfaz para que el usuario interactúe con el sistema.

class CifradoCesar:
    def __init__(self, clave):
        self.clave = clave

    def encriptar(self, texto):
        resultado = ''
        for char in texto:
            if char.isalpha():
                desplazamiento = self.clave % 26
                if char.islower():
                    base = ord('a')
                    resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
                else:
                    base = ord('A')
                    resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
            else:
                resultado += char
        return resultado

    def desencriptar(self, texto):
        return self.encriptar(texto, -self.clave)

# Uso del cifrado
clave = 3  # Clave de desplazamiento
cifrador = CifradoCesar(clave)

texto = "Hola Mundo"
texto_encriptado = cifrador.encriptar(texto)
print("Texto encriptado:", texto_encriptado)
texto_desencriptado = cifrador.desencriptar(texto_encriptado)
print("Texto desencriptado:", texto_desencriptado)