# Ejercicio compuesto con if
print("calcular el promedio de un alumno")
nombre = input("como te llamas: ")
seguridad_aeropertuaria = int(input(nombre + " cual es tu calificacion en seguridad aeropertuaria: "))
seguridad_de_instalaciones = int(input(nombre + " cual es tu calificacion en seguridad de instalaciones: "))
sistema_de_armamento = int(input(nombre + " cual es tu calificacion en sistema de armamento: "))
promedio = (seguridad_aeropertuaria + seguridad_de_instalaciones + sistema_de_armamento) / 3
promedio = int(promedio)
if promedio >= 70:
   print("felicidades " , nombre, " tu promedio de esta clases es de: " , promedio)
print("fin.")