while True:
    edad = int(input("Ingrese su edad: "))
    if edad < 3:
        print("Entrada gratis")
    elif edad >= 3 and edad <= 12:
        print("La entrada cuesta 10 pesitos.")
    else:
        print("La entrada cuesta 15 pesitos.")