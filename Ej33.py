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

class PuestoDeHelados(Restaurante):
    def __init__(self, nombre, tipo_cocina, sabor):
        super().__init__(nombre, tipo_cocina)
        self.sabores = sabor
    def mostrar_sabores(self):
        print("Sabores:")
        for e in self.sabores:
            print(e)

amarusin = Restaurante("Los Amarusines Bebes", "Italiana")
helados_amarusin = PuestoDeHelados("Los Amarusines Bebes", "Heladería", ["Frutilla", "Vainilla", "Chocolate"])
helados_amarusin.mostrar_sabores()
