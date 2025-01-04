'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SISTEMA DE GESTION DE CLIENTES
'''

# Crea un sistema para gestionar clientes, que permite agregar, buscar y eliminar clientes.

# PASOS
# Paso 1: Define una clase Cliente que contenga información como nombre, email, y teléfono.
# Paso 2: Crea una clase GestionClientes que permite gestionar una lista de clientes.
# Paso 3: Implementa métodos para agregar, buscar y eliminar clientes.
# Paso 4: Proporciona una consola para interactuar con el sistema.

class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} - {self.email} - {self.telefono}"

class GestionClientes:
    def __init__(self):
        self.clientes = {}

    def agregar_cliente(self, cliente):
        self.clientes[cliente.email] = cliente

    def buscar_cliente(self, email):
        return self.clientes.get(email, None)

    def eliminar_cliente(self, email):
        if email in self.clientes:
            del self.clientes[email]

# Uso del sistema de gestión de clientes
gestion = GestionClientes()
cliente1 = Cliente("Carlos", "carlos@example.com", "123456789")
cliente2 = Cliente("Ana", "ana@example.com", "987654321")

gestion.agregar_cliente(cliente1)
gestion.agregar_cliente(cliente2)

print("Buscar cliente con email 'carlos@example.com':")
cliente_encontrado = gestion.buscar_cliente("carlos@example.com")
print(cliente_encontrado)

gestion.eliminar_cliente("ana@example.com")
print("Buscar cliente eliminado:")
print(gestion.buscar_cliente("ana@example.com"))