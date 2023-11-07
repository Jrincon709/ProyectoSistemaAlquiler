class Saldo_Insuficiente_Error(Exception):
    def __init__(self, saldo: int ,total_carrito):
        self.saldo = saldo
        self.total_carrito= total_carrito

    def __str__(self):
        return (f"Tu saldo actualmente es de {self.saldo} no es suficiente para pagar el total"
                f"de tu carrito que es {self.total_carrito}")
