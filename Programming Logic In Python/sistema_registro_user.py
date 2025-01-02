'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SISTEMA DE REGISTRO DE USUARIOS
'''

# Crea un sistema que permite registrar usuarios y autenticar su acceso.

# PASOS
# Paso 1: Define una clase Usuario que contenga atributos como nombre, email y contraseña.
# Paso 2: Crea una clase SistemaRegistro que mantenga una lista de usuarios.
# Paso 3: Agrega métodos para registrar y autenticar usuarios.
# Paso 4: Implementa una función para mostrar los usuarios registrados

class Usuario:
    def __init__(self, nombre, email, contrasena):
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena

class SistemaRegistro:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, nombre, email, contrasena):
        if email in self.usuarios:
            print("Usuario ya registrado.")
        else:
            self.usuarios[email] = Usuario(nombre, email, contrasena)
            print("Usuario registrado exitosamente.")

    def autenticar(self, email, contrasena):
        usuario = self.usuarios.get(email)
        if usuario and usuario.contrasena == contrasena:
            print(f"Bienvenido {usuario.nombre}!")
        else:
            print("Email o contraseña incorrectos.")

    def mostrar_usuarios(self):
        for usuario in self.usuarios.values():
            print(f"Nombre: {usuario.nombre}, Email: {usuario.email}")

# Uso del sistema de registro
sistema = SistemaRegistro()
sistema.registrar_usuario('Alice', 'alice@example.com', 'password123')
sistema.registrar_usuario('Bob', 'bob@example.com', 'qwerty')
sistema.mostrar_usuarios()
sistema.autenticar('alice@example.com', 'password123')