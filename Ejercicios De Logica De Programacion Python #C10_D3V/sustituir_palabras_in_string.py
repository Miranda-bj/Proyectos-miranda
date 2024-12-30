'''
EJERCICIO DE LOGICA DE PROGRAMACION
SUSTITUIR PALABRAS EN UNA CADENA
'''
def sustituir_palabra(cadena, vieja, nueva):
    return cadena.replace(vieja, nueva)
print(sustituir_palabra("Hola Mundo", "Mundo", "C10_D3V"))
# Explicación:
# Definimos la función sustituir_palabra que toma una cadena, una palabra vieja y una nueva.
# Usamos el método replace() para sustituir todas las ocurrencias de la palabra vieja por la nueva en la cadena.
# Retornamos la cadena modificada.
# Probamos la función con "Hola Mundo" y sustituimos "Mundo" por "C10_D3V".