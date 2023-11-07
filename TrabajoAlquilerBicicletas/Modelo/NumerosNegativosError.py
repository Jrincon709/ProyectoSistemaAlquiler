
class NumerosNegativosError (Exception):
    def __init__(self,numero):
        self.numero=numero

    def __str__(self):
        return "No se permiten números negativos"

    @staticmethod
    def validar_numero_negativo(numero):
        if numero < 0:
            raise NumerosNegativosError(numero)
        return numero

