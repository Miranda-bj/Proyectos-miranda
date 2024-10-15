# sentencia condicional if elif
print("sistema para calcular el promedio de un alumno")

nombre = input("introduce un nombre y un apellido: ")

seguridad_aeropertuaria = float(input(nombre + " introduce tu nota total de seguridad aeropertuaria: "))
seguridad_de_instalaciones = float(input(nombre + " introduce tu nota total de seguridad de instalaciones: "))
sistema_de_armamento = float(input(nombre + " introduce tu nota total de sistema de armamento: "))
inteligencia_aerea = float(input(nombre + " introduce tu nota total de inteligencia aerea: "))

promedio = (seguridad_aeropertuaria + seguridad_de_instalaciones + sistema_de_armamento + inteligencia_aerea) / 4

if promedio >= 70:
     print("felicidades " + nombre + " aprobaste el periodo con un promedio de: ", promedio)
     print("felicidades " + nombre + " aprobaste el periodo con un promedio de: ", round(promedio, 2))
else:
     print(nombre + " has reprobado el periodo con un promedio de: ", promedio)
     print(nombre + " has reprobado el periodo con un promedio de: ", round(promedio, 1))
print("fin.")
