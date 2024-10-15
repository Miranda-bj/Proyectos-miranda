# Calculadora funcional
def sumar(x, y):
  """Suma dos números."""
  return x + y

def restar(x, y):
  """Resta dos números."""
  return x - y

def multiplicar(x, y):
  """Multiplica dos números."""
  return x * y

def dividir(x, y):
  """Divide dos números."""
  if y == 0:
    return "No se puede dividir por cero"
  else:
    return x / y

while True:
  print("Seleccione la operación:")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")
  print("5. Salir")

  eleccion = input("Ingrese el número de la operación (1/2/3/4/5): ")

  if eleccion in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Ingrese el primer número: "))
      num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
      print("Entrada inválida. Ingrese números válidos.")
      continue

    if eleccion == '1':
      print(num1, "+", num2, "=", sumar(num1, num2))

    elif eleccion == '2':
      print(num1, "-", num2, "=", restar(num1, num2))

    elif eleccion == '3':
      print(num1, "*", num2, "=", multiplicar(num1, num2))

    elif eleccion == '4':
      print(num1, "/", num2, "=", dividir(num1, num2))

  elif eleccion == '5':
    break
  else:
    print("Opción inválida. Intente nuevamente.")