'''
EJERCICIO DE LOGICA DE PROGRAMACION
CALCULAR EL FACTORIAL DE UN NUMERO
'''
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))
# Explicación:
# Definimos la función factorial que calcula el factorial de n.
# Si n es 0, el factorial es 1.
# En caso contrario, multiplicamos n por el factorial de n-1.
# Probamos la función con el número 5.