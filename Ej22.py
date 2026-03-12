while True:
    print("Escriba 'salir' para parar!")
    ing = input("Ingrese un ingrediente para la pizza: ")
    if ing.lower() == "salir":
        break
    else:
        print(f"Se añadió {ing}!")