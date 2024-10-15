# COMPARACION DE NUMEROS CON OPERADORES RELACIONALES
print("==================================")
print("Introduce dos numeros a comparar: ")
print("==================================")

num_uno = int(input("Escriba el primer numero: "))
num_dos = int(input("Escriba el segundo numero: "))

print("Los numeros a comparar son", num_uno, " y ", num_dos)

if num_uno == num_dos:
    print("Es igual....")
if num_uno != num_dos:
    print("Es diferente....")
if num_uno > num_dos:
    print("Es mayor....")
if num_uno < num_dos:
    print("Es menor....")
if num_uno >= num_dos:
    print("Es mayor o igual....")
if num_uno <= num_dos:
    print("Es menor o igual....")

print("Fin de las comparaciones")
