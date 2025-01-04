'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SISTEMA DE CHAT SIMULADO
'''

# Crea un sistema que permite simular un chat entre varios usuarios.

# PASOS
# Paso 1: Define una clase Usuario que tenga un nombre y un método para enviar mensajes.
# Paso 2: Crea una clase Chat que mantenga un registro de usuarios y mensajes.
# Paso 3: Implementa métodos para enviar y mostrar mensajes en el chat.
# Paso 4: Proporciona un menú de consola que permita interactuar con el sistema de chat.

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def enviar_mensaje(self, chat, mensaje):
        chat.agregar_mensaje(self, mensaje)

class Chat:
    def __init__(self):
        self.mensajes = []

    def agregar_mensaje(self, usuario, mensaje):
        self.mensajes.append(f"{usuario.nombre}: {mensaje}")

    def mostrar_mensajes(self):
        for mensaje in self.mensajes:
            print(mensaje)

# Uso del chat
chat = Chat()
usuario1 = Usuario("Alice")
usuario2 = Usuario("Bob")

while True:
    print("1. Enviar mensaje")
    print("2. Mostrar mensajes")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        usuario = input("Introduce tu nombre: ")
        mensaje = input("Introduce tu mensaje: ")
        if usuario == "Alice":
            usuario1.enviar_mensaje(chat, mensaje)
        elif usuario == "Bob":
            usuario2.enviar_mensaje(chat, mensaje)
    elif opcion == '2':
        chat.mostrar_mensajes()
    elif opcion == '3':
        break
    else:
        print("Opción no válida.")