

class BicicletaError(Exception):
    def __init__(self, id_pedido:int):
        self.id_pedido:int = id_pedido
