import datetime
class Transaccion:
    def __init__(self, codigo:int,bicicletas:list,fecha:'datetime',valor_total:int):
        self.codigo = codigo
        self.bicicletas = bicicletas

        self.valor_total =valor_total

        self.fecha = fecha
    def __str__(self) -> str:
        valor_formateado = "${:,.0f}".format (self.valor_total)
        bicicletas_alquiladas = ', '.join (map (str, self.bicicletas))
        return f"Transaccion N° {self.codigo}. \n El dia {self.fecha}, Usted realizo una compra de las bicicletas alquiladas:\n {bicicletas_alquiladas} con un costo total de: {valor_formateado}"

