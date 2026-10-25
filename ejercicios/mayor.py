# Enunciado: escribir una función que reciba dos edades y devuelva
# la mayor. Después, usarla para mostrar cuál es la edad mayor.
def mayor(a, b):
    if a >= b:
        return a
    return b

while True:
    try:
        edad1 = int(input("Edad 1: "))
        if edad1 <= 0:
            raise ValueError
        edad2 = int(input("Edad 2: "))
        if edad2 <= 0:
            raise ValueError
        resultado = mayor(edad1, edad2)
        if edad1 == edad2:
            print("Las edades son iguales")
        else:
            print(f"La edad mayor es: {resultado}")
        break
    except ValueError:
        print("Error, las edades deben ser números mayores que 0")