'''
EJERCICIO DE LOGICA DE PROGRAMACION
CONTAR LA CANTIDAD DE PALABRAS EN UNA FRASE
'''
def contar_palabras(frase):
    return len(frase.split())
print(contar_palabras("Hola Mundo Con Python, ¿cómo están?"))
# Explicación:
# Definimos la función contar_palabras que recibe una frase.
# Usamos el método split() para separar la frase en palabras.
# Retornamos la longitud de la lista resultante, que es el número de palabras.
# Probamos la función con "Hola Mundo Con Python, ¿cómo están?"