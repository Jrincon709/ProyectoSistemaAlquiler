
from TrabajoAlquilerBicicletas.Modelo.Bicicleta import Bicicleta
class Item:
    def __init__(self, bicicleta: 'Bicicleta', horas_a_alquilar:int):
        self.bicicleta = bicicleta
        self.horas_a_alquilar = horas_a_alquilar

    def calcular_subtotal (self):
        return self.bicicleta.valor_hora * self.horas_a_alquilar

    def __str__(self):

        return f"Bicicleta con Id: {self.bicicleta.id}  Modelo: {self.bicicleta.tipo} Cantidad de horas a alquilar: {self.horas_a_alquilar} Costo: {self.calcular_subtotal()}"