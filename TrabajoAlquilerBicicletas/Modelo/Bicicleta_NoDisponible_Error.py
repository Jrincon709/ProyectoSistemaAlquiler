
from TrabajoAlquilerBicicletas.Modelo.Bicicleta_Error import BicicletaError
class BicicletaNoDisponibleError(BicicletaError):
    def __init__(self, id_pedido: int):
        super ().__init__ (id_pedido)

    def __str__(self):
        return f"La Bicicleta con el id {self.id_pedido} no se encuentra en tu carro de compras"

