import json
num = input("Cual es tu número favorito? ")

with open("num_fav.json", "w") as file:
    file.write(json.dumps(num))