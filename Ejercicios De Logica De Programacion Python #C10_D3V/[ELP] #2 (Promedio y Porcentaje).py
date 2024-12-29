'''
EJERCICIO DE LOGICA DE PROGRAMACION:
Crea un programa que pida al usuario su promedio de calificaciones
y el porcentaje de asistencia a clases. Para aprobar el curso,
el estudiante debe tener un promedio mayor o igual a 70 y una
asistencia minima del 80%. Si el estudiante cumple ambos
criterios, imprime 'aprobado'. Si solo uno de los criterios
es cumplido, imprime 'Aprobado Condicional'.
Si ninguno de los criterios es cumplido, imprime 'reprobado'.
'''
print("\t*******************************************")
print("\t****ejercicio de logica de programacion****".upper())
print("\t*******************************************\n")

usuario = input("Introduce tu nombre: ")
promedio = int(input("Introduce tu promedio de calificaciones: "))
porcentaje = int(input("Introduce tu porcentaje de asistencia a clases: "))

if promedio >= 70 and porcentaje >= 80:
  print(f"Bien {usuario} has 'aprobado'.")
elif promedio >= 70 or porcentaje >= 80:
  print(f"Bien {usuario} has 'Aprobado Condicionalmente'")
else:
  promedio <= 70 or porcentaje <= 80
  print(f"Mal {usuario} has 'Reprobado'")