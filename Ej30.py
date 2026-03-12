class Restaurante:
    def __init__(self, nombre, tipo_cocina):
        self.nombre = nombre
        self.tipo = tipo_cocina
    def describir_restaurante(self):
        print(f"Nombre del restaurante: {self.nombre}\nTipo de cocina: {self.tipo}")
    def abrir_restaurante(self):
        print("El restaurante está abierto")

amarusin = Restaurante("Los Amarusines Bebes", "Italiana")
amarusin.describir_restaurante()
amarusin.abrir_restaurante()