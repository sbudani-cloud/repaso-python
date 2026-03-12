class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def describir_usuario(self):
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}")
    def saludar_usuario(self):
        print(f"Hola {self.nombre}!! Buenos dias :3")

luli = Usuario("Lucía", "Budani")
amarusin = Usuario("Amaru", "Budani")
mati = Usuario("Matías", "Budani")
rami = Usuario("Ramiro", "Budani")

luli.describir_usuario()
luli.saludar_usuario()

amarusin.describir_usuario()
amarusin.saludar_usuario()

mati.describir_usuario()
mati.saludar_usuario()

rami.describir_usuario()
rami.saludar_usuario()