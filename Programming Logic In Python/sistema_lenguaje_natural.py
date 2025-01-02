'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SISTEMA DE LENGUAJE NATURAL
'''

# Crea un sistema que permita realizar análisis de texto básico, como contar palabras y verificar la gramática simple.

# PASOS
# Paso 1: Define una clase AnalizadorTexto que contenga un método para contar palabras y un método para verificar frases.
# Paso 2: Implementa un método que permita recibir texto como entrada.
# Paso 3: Agrega funcionalidades adicionales, como contar caracteres y encontrar palabras clave.
# Paso 4: Proporciona un menú para que el usuario interactúe con el sistema.

class AnalizadorTexto:
    def __init__(self, texto):
        self.texto = texto

    def contar_palabras(self):
        return len(self.texto.split())

    def contar_caracteres(self):
        return len(self.texto)

    def verificar_frase(self):
        if self.texto.endswith('.'):
            return "Frase correcta."
        else:
            return "Frase incorrecta, debe terminar con un punto."

def menu():
    while True:
        texto = input("Introduce el texto (o 'salir' para terminar): ")
        if texto.lower() == 'salir':
            break
        analizador = AnalizadorTexto(texto)
        print("Número de palabras:", analizador.contar_palabras())
        print("Número de caracteres:", analizador.contar_caracteres())
        print(analizador.verificar_frase())

# Ejecutar el menú
menu()