
class Bicicleta:
    def __init__(self, id:int, tipo:str, color:str, valor_hora:int ):
        self.id:int = id
        self.tipo:str = tipo
        self.color:str = color
        self.valor_hora:int = valor_hora
    def __str__(self) -> str:
        valor_formateado = "${:,.0f}".format (self.valor_hora)
        return f"ID: {self.id} Tipo: {self.tipo} Color: {self.color} Valor hora: {valor_formateado}"

