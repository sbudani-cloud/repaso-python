#Con prueba condicional en el while:
"""
edad = 0
while edad != 666:
    edad = int(input("Ingrese su edad: "))
    if edad == 666:
        pass
    elif edad < 3:
        print("Entrada gratis")
    elif edad >= 3 and edad <= 12:
        print("La entrada cuesta 10 pesitos.")
    else:
        print("La entrada cuesta 15 pesitos.")
"""

#Con variable de control:
"""
cont = 0
while cont < 3:
    edad = int(input("Ingrese su edad: "))
    if edad < 3:
        print("Entrada gratis")
    elif edad >= 3 and edad <= 12:
        print("La entrada cuesta 10 pesitos.")
    else:
        print("La entrada cuesta 15 pesitos.")
    cont += 1
"""

#Con break:
"""
while True:
    edad = input("Ingrese su edad: ")
    if edad.lower() == "salir":
        break
    elif int(edad) < 3:
        print("Entrada gratis")
    elif int(edad) >= 3 and int(edad) <= 12:
        print("La entrada cuesta 10 pesitos.")
    else:
        print("La entrada cuesta 15 pesitos.")
"""