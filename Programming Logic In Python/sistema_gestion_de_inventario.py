'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SISTEMA DE GESTION DE INVENTARIO
'''

# Crea un sistema que permite gestionar un inventario de productos mediante operaciones de agregar, eliminar y listar productos.

# PASOS
# Paso 1: Define una clase Producto que contenga atributos como id, nombre y cantidad.
# Paso 2: Crea una clase Inventario que mantenga una lista de productos.
# Paso 3: Implementa métodos para agregar, eliminar y listar productos.
# Paso 4: Agrega funcionalidad para restar y sumar productos.

class Producto:
    def __init__(self, id: int, nombre: str, cantidad: int):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad

    def __repr__(self):
        return f"{self.nombre} (ID: {self.id}, Cantidad: {self.cantidad})"

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto: Producto):
        if producto.id in self.productos:
            self.productos[producto.id].cantidad += producto.cantidad
        else:
            self.productos[producto.id] = producto

    def eliminar_producto(self, id: int):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado.")

    def listar_productos(self):
        for producto in self.productos.values():
            print(producto)

    def actualizar_cantidad(self, id: int, cantidad: int):
        if id in self.productos:
            self.productos[id].cantidad += cantidad
        else:
            print("Producto no encontrado.")

# Uso del inventario
inventario = Inventario()
inventario.agregar_producto(Producto(1, 'Laptop', 10))
inventario.agregar_producto(Producto(2, 'Teléfono', 20))
inventario.actualizar_cantidad(1, -2)
inventario.listar_productos()
inventario.eliminar_producto(2)
inventario.listar_productos()