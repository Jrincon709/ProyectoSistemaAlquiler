from TrabajoAlquilerBicicletas.Modelo.Bicicleta import Bicicleta
from TrabajoAlquilerBicicletas.Modelo.Bicicleta_Error import BicicletaError
class BicicletaExistenteError(BicicletaError):
    def __init__(self, id_pedido: int):
        super().__init__(id_pedido)

    def __str__(self):
        return (f"La Bicicleta con el id {self.id_pedido} no existe o no se encuentra disponible"
                f"en este momento")

