'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SISTEMA DE REGISTRO DE VENTAS
'''

# Crea un sistema de registro de ventas que permita a los usuarios ingresar detalles de ventas y calcular el total de las mismas.

# PASOS
# Paso 1: Define una clase Venta que contenga información sobre el producto, cantidad y precio.
# Paso 2: Crea una clase SistemaVentas que mantenga un registro de las ventas.
# Paso 3: Implementa métodos para agregar ventas y calcular el total.
# Paso 4: Proporciona una interfaz para agregar y mostrar ventas

class Venta:
    def __init__(self, producto, cantidad, precio):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

    def total(self):
        return self.cantidad * self.precio

class SistemaVentas:
    def __init__(self):
        self.ventas = []

    def agregar_venta(self, producto, cantidad, precio):
        venta = Venta(producto, cantidad, precio)
        self.ventas.append(venta)

    def calcular_total(self):
        return sum(venta.total() for venta in self.ventas)

    def mostrar_ventas(self):
        for venta in self.ventas:
            print(f"Producto: {venta.producto}, Cantidad: {venta.cantidad}, Precio: {venta.precio}, Total: {venta.total()}")

# Uso del sistema de ventas
sistema = SistemaVentas()
sistema.agregar_venta("Laptop", 1, 1000)
sistema.agregar_venta("Teléfono", 2, 500)
sistema.mostrar_ventas()
print("Total de las ventas:", sistema.calcular_total())