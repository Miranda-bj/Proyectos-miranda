'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SISTEMA DE CALCULADORA
'''

# Crea una calculadora que realice operaciones básicas y permita la extensión de nuevas operaciones.

# PASOS
# Paso 1: Define una clase Calculadora que implemente métodos para operaciones como suma, resta, multiplicación y división.
# Paso 2: Implementa un método para agregar operaciones personalizadas con funciones de entrada.
# Paso 3: Proporciona una interfaz de línea de comandos para recibir entradas del usuario.
# Paso 4: Maneja excepciones y errores de entrada.

class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return a / b

    def agregar_operacion(self, nombre, funcion):
        setattr(self, nombre, funcion)

# Uso de la calculadora
calc = Calculadora()
print("Suma (2 + 3):", calc.suma(2, 3))
print("Resta (5 - 2):", calc.resta(5, 2))
print("Multiplicación (4 * 3):", calc.multiplicacion(4, 3))
print("División (10 / 2):", calc.division(10, 2))

# Agregar una operación personalizada
def potencia(a, b):
    return a ** b

calc.agregar_operacion("potencia", potencia)
print("Potencia (2 ** 3):", calc.potencia(2, 3))