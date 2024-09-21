#Uso de excepciones
try:
    num1 = int(input("Ingresa el primer número entero: "))
    num2 = int(input("Ingresa el segundo número entero: "))

    suma = num1 + num2
    print("La suma de los números ingresados es:", suma)

    if num2 == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    division = num1 / num2
    print("La división es:", division)

except ValueError:
    print("Error: Ingresaste un valor no numérico.")
except ZeroDivisionError as e:
    print(e)
