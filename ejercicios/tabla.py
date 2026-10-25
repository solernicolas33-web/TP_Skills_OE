# Enunciado: pedir un número al usuario y mostrar su tabla
# de multiplicar, del 1 al 10.
while True:
    try:
        numero = int(input("Ingresá un número: "))
    except ValueError:
        print("Error, se debe ingresar un número entero")
        continue
    for i in range(1,11):
        print(f"{numero} * {i} = {numero * i}")
    break