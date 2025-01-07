'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SIMULADOR DE COMPRAS EN LINEA
'''

# Crea un sistema que simula el proceso de compra en línea, donde los usuarios
# pueden agregar productos al carrito y realizar pagos.

# PASOS
# Paso 1: Define una clase Producto que contenga información básica sobre el producto.
# Paso 2: Crea una clase Carrito para gestionar los productos agregados.
# Paso 3: Añade métodos para agregar productos, calcular el total y realizar el pago.
# Paso 4: Proporciona una interfaz simple para interactuar con el sistema.

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}: ${self.precio}"

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def obtener_total(self):
        return sum(producto.precio for producto in self.productos)

    def realizar_pago(self):
        total = self.obtener_total()
        print(f"Total a pagar: ${total:.2f}")
        if total > 0:
            print("Pago realizado con éxito.")
        else:
            print("No hay productos en el carrito.")

# Uso del sistema de compras
carrito = Carrito()
producto1 = Producto("Lapiz", 0.5)
producto2 = Producto("Cuaderno", 3.0)

carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)

print("Productos en el carrito:")
for producto in carrito.productos:
    print(producto)

carrito.realizar_pago()