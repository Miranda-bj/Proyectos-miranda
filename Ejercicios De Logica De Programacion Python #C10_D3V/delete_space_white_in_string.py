'''
EJERCICIO DE LOGICA DE PROGRAMACION
ELIMINAR ESPACIO EN BLANCO DE UNA CADENA
'''
def eliminar_espacios(cadena):
    return ''.join(cadena.split())
print(eliminar_espacios("  Hola   Mundo  "))
# Explicación:
# Definimos la función eliminar_espacios que recibe una cadena.
# Usamos split() para dividir la cadena y luego join() para unirla sin espacios.
# Retornamos la nueva cadena sin espacios.
# Probamos la función con una cadena que contiene múltiples espacios.