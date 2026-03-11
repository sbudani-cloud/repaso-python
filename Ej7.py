import random
colores = ["verde", "rojo", "amarillo", "rosa", "fucsia"]
color = random.randint(0, 4)
color_alien = colores[color]
if color_alien == "verde":
    print("Ganaste 5 puntos")
elif color_alien == "amarillo":
    print("Ganaste 10 puntos")
elif color_alien == "rojo":
    print("Ganaste 15 puntos")
else:
    print("Ganaste 0 puntos")