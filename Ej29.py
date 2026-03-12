#Ejercicios para hacer (nº de diapositiva): 175, 193, 195, 205, 223, 232, 262, 288, 
#312, 315, 348, 349
def auto(fabr, mod, **info_auto):
    print(f"El auto modelo {mod}, fabricado por {fabr}, tiene las siguientes caracteristicas:")
    for e in info_auto:
        print(f"{e.title()} : {info_auto[e]}")

auto("amarusin", "toyota", color = "rosa", airbags = True)