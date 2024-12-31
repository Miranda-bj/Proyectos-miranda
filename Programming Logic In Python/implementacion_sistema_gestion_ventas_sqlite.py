'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SISTEMA DE GESTION DE VENTAS CON SQLITE
'''
# Crea una aplicación que permita gestionar productos y realizar ventas utilizando SQLite como base de datos.

# Pasos
# Paso 1: Configura una base de datos SQLite y crea tablas para productos y ventas.
# Paso 2: Define funciones para añadir productos y registrar ventas.
# Paso 3: Implementa una interfaz de línea de comandos para interactuar con la aplicación.
# Paso 4: Agrega validaciones y maneja excepciones.

import sqlite3

def crear_base_datos():
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos
                      (id INTEGER PRIMARY KEY, nombre TEXT, precio REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS ventas
                      (id INTEGER PRIMARY KEY, producto_id INTEGER, cantidad INTEGER,
                      FOREIGN KEY (producto_id) REFERENCES productos(id))''')
    conn.commit()
    conn.close()

def agregar_producto(nombre, precio):
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO productos (nombre, precio) VALUES (?, ?)', (nombre, precio))
    conn.commit()
    conn.close()

def registrar_venta(producto_id, cantidad):
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ventas (producto_id, cantidad) VALUES (?, ?)', (producto_id, cantidad))
    conn.commit()
    conn.close()

def listar_productos():
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    conn.close()
    return productos

def menu():
    crear_base_datos()
    while True:
        print("\n--- Gestión de Ventas ---")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Registrar venta")
        print("4. Salir")
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            agregar_producto(nombre, precio)
        elif opcion == 2:
            productos = listar_productos()
            for p in productos:
                print(f'ID: {p[0]}, Nombre: {p[1]}, Precio: ${p[2]:.2f}')
        elif opcion == 3:
            producto_id = int(input("ID del producto: "))
            cantidad = int(input("Cantidad vendida: "))
            registrar_venta(producto_id, cantidad)
        elif opcion == 4:
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    menu()