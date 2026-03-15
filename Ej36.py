listo = False
while not listo:
    try:
        a = int(input("Ingrese un número: "))
    except ValueError:
        print("Eso no es un número amiguito...")
    else:
        try:
            b = int(input("Ingrese otro número: "))
        except ValueError:
            print("Eso no es un número amiguito...")
        else:
            listo = True
            print(f"El resultado es {a+b}.")