# SISTEMA PARA CALCULAR EL PROMEDIO DE UN ALUMNO
print("=================================")
print("Calcular el promedio de un alumno")
print("=================================")

nombre = input("Ingrese su nombre y su apellido: ")

seguridad_de_instalaciones = int(input(nombre + " Ingresa la nota de seguridad de instalaciones aereas: "))
seguridad_aeropertuaria = int(input(nombre + " Ingresa la nota de seguridad aeropertuaria: "))
inteligencia_aerea = int(input(nombre + " Ingresa la nota de inteligencia aerea: "))
sistema_de_armamento = int(input(nombre + " Ingresa la nota de sistema de armamento: "))

promedio = (seguridad_de_instalaciones + seguridad_aeropertuaria + inteligencia_aerea + sistema_de_armamento) / 4
promedio = int(promedio)

if promedio >= 70:
    print("=================================================================")
    print("excelente " + nombre + " Has aprobado con un promedio de: ", promedio)
    print("=================================================================")
else:
    print("======================================================")
    print(nombre + " Has reprobado con un promedio de: ", promedio)
    print("======================================================")

print("FIN DEL PROGRAMA.")
    