sanguches_pedidos = ["Jamón y queso", "Atún", "Milanesa", "BLT", "Lomito", "Vegetariano"]
sanguches_terminados = []
while sanguches_pedidos:
    sanguchito = sanguches_pedidos.pop()
    print(f"Tu sanguche de {sanguchito} está listo!")
    sanguches_terminados.append(sanguchito)
    input()
print(sanguches_terminados)
