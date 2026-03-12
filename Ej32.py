#Ejercicios para hacer (nº de diapositiva): 205, 223, 232, 262, 288, 312, 315, 348, 349\
class Restaurante:
    def __init__(self, nombre, tipo_cocina):
        self.nombre = nombre
        self.tipo = tipo_cocina
        self.clientes_atendidos = 0
    def describir_restaurante(self):
        print(f"Nombre del restaurante: {self.nombre}\nTipo de cocina: {self.tipo}\nClientes atendidos: {self.clientes_atendidos}")
    def abrir_restaurante(self):
        print("El restaurante está abierto")
    def establecer_clientes_atendidos(self, num):
        self.clientes_atendidos = num
    def incrementar_clientes_atendidos(self, num):
        self.clientes_atendidos += num

amarusin = Restaurante("Los Amarusines Bebes", "Italiana")
amarusin.describir_restaurante()
amarusin.abrir_restaurante()
amarusin.establecer_clientes_atendidos(4)
amarusin.incrementar_clientes_atendidos(2)
amarusin.describir_restaurante()