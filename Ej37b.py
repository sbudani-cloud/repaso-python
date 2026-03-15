import json

with open("num_fav.json", "r") as file:
    num = json.loads(file.read())

print(f"Tu número favorito es {num}!")