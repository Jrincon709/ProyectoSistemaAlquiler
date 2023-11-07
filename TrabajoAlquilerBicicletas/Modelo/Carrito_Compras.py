
from TrabajoAlquilerBicicletas.Modelo.Bicicleta import Bicicleta
from TrabajoAlquilerBicicletas.Modelo.Item import Item

class Carrito_compras:


    def __init__(self) -> None:
        self.items: list[Item] = []

    def agregar_item(self,bicicleta:Bicicleta,tiempo:int):
        item = Item(bicicleta, tiempo)
        self.items.append(item)
        return item

    def calcular_costo_total(self):
        total = 0
        for i in self.items:
            total += i.calcular_subtotal()
        return total

    def quitar_item(self, id):
        self.items =[ item for item in self.items if id != item.bicicleta.id]

    def mostrar_carrito(self):
        for item in self.items:
            print (item)


