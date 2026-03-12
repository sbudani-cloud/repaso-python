
sanguches_pedidos = ["Jamón y queso", "Pastrón", "Atún", "Milanesa", "Pastrón", "BLT", "Lomito", "Pastrón", "Vegetariano"]
sanguches_terminados = []
print("Nos quedamos sin Pastrón")
while sanguches_pedidos:
    sanguchito = sanguches_pedidos.pop()
    if sanguchito == "Pastrón":
        pass
    else:
        print(f"Tu sanguche de {sanguchito} está listo!")
        sanguches_terminados.append(sanguchito)
        input()
print(sanguches_terminados)
