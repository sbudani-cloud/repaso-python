#Ejercicios para hacer (nº de diapositiva): 262, 288, 312, 315, 348, 349\
nombres = []
while True:
    nombre = input("Ingrese su nombre (o escriba 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    else:
        nombres.append(nombre)

with open("guest_book.txt", "w") as archivo:
    for n in nombres:
        archivo.write(n+"\n")