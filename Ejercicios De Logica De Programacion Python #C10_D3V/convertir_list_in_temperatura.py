'''
EJERCICIO DE LOGICA DE PROGRAMACION
CONVERTIR UNA LISTA DE TEMPERATURAS DE CELSIUS A FAHRENHEIT
'''
def celsius_a_fahrenheit(celsius):
    return [(temp * 9/5) + 32 for temp in celsius]
print(celsius_a_fahrenheit([0, 25, 100]))
# Explicación:
# Definimos la función celsius_a_fahrenheit, que recibe una lista de temperaturas en Celsius.
# Usamos una comprensión de lista para convertir cada temperatura a Fahrenheit usando la fórmula.
# Retornamos la lista de temperaturas convertidas.
# Probamos la función con una lista que incluye 0, 25 y 100 grados Celsius.