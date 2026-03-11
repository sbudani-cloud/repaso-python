import random
colores = ["verde", "rojo"]
color = random.randint(0, 1)
color_alien = colores[color]
if color_alien == "verde":
    print("Ganaste 5 puntos")