#Ejercicios para hacer (nº de diapositiva): 315, 348, 349\
from pathlib import Path 
import json

def obtener_usuario_guardado(path):
    if path.exists():
        contenido = path.read_text()
        user = json.loads(contenido)
        return user
    else:
        return None

def obtener_nuevo_usuario(path):
    #Pide un nuevo nombre de usuario.
    nombre = input("¿Cómo te llamás? ")
    edad = input("¿Cuantos años tenes?")
    ciud = input("¿En qué ciudad vivis?")

    user = {
        "Nombre" : nombre,
        "Edad" : edad,
        "Ciudad" : ciud
    }

    contenido = json.dumps(user)
    path.write_text(contenido)
    return user

def saludar_usuario():
    #Saluda a la persona usuaria por su nombre.
    path = Path('username.json')
    user= obtener_usuario_guardado(path)
    if user:
        print(f"¡Bienvenido de nuevo, {user['Nombre'].title()}!")
        print(f"Me acuerdo que tenes {user['Edad']} años y vivis en {user['Ciudad']}")
    else:
        user= obtener_nuevo_usuario(path)
        print(f"Te vamos a recordar cuando vuelvas, {user['Nombre'].title()}.")

saludar_usuario()
