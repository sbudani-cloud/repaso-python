def auto(fabr, mod, **info_auto):
    print(f"El auto modelo {mod}, fabricado por {fabr}, tiene las siguientes caracteristicas:")
    for e in info_auto:
        print(f"{e.title()} : {info_auto[e]}")

auto("amarusin", "toyota", color = "rosa", airbags = True)