glosario = {
    "sorted()" : "Función que devuelve una lista ordenada sin modificarla.",
    "len()" : "Función que devuelve la cantidad de elementos en una lista o carácteres en un string.",
    "print()" : "Función que muestra en la terminal lo que se le asigne en los parentesis.",
    "if" : "Estructura para comparar datos y dependiendo del resultado ir en distinas diredcciones.",
    "range()" : "Funcion que permite generar numeros dentro de un rango que se asigna en los parentesis."
}

for e in glosario:
    print(f"{e.title()}\n   {glosario[e]}\n")