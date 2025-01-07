'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN ANALIZADOR DE ARCHIVOS CSV
'''

# Crea un analizador que lea archivos CSV y los convierta en una lista de diccionarios.

# PASOS
# Paso 1: Define una función que toma el nombre del archivo y las claves basado en la primera línea del CSV.
# Paso 2: Lee el archivo línea por línea y convierte cada línea en un diccionario.
# Paso 3: Maneja el caso donde se produzcan excepciones durante la lectura de archivos.
# Paso 4: Proporciona un ejemplo de uso.

import csv

def leer_csv(nombre_archivo):
    with open(nombre_archivo, mode='r', encoding='utf-8') as file:
        lector = csv.reader(file)
        headers = next(lector)
        resultados = []

        for fila in lector:
            if len(fila) == len(headers):
                diccionario = {headers[i]: fila[i] for i in range(len(headers))}
                resultados.append(diccionario)
            else:
                print("Fila ignorada debido a discrepancia en número de columnas.")

        return resultados

# Uso del analizador CSV
archivo_csv = "ejemplo.csv"
resultados = leer_csv(archivo_csv)
for registro in resultados:
    print(registro)