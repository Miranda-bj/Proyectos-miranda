while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        op = input("Ingrese la operación (+, -, *, /): ")
        num2 = float(input("Ingrese el segundo número: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("No se puede dividir entre cero.")
            else:
                result = num1 / num2
        else:
            print("Operación inválida.")
            continue

        print("Resultado:", result)
        break  # Salir del bucle si la operación se realiza correctamente

    except ValueError:
        print("Entrada inválida. Ingrese números válidos.")