
from TrabajoAlquilerBicicletas.Modelo.Bicicleta_Error import BicicletaError
class Bicicleta_No_En_Posecion(BicicletaError):
    def __init__(self, id_pedido: int):
        super ().__init__ (id_pedido)

    def __str__(self):
        return f"No has alquilado la Bicicleta con el id {self.id_pedido} "

