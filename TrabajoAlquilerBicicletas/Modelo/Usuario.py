from TrabajoAlquilerBicicletas.Modelo.Transacciones import Transaccion
from TrabajoAlquilerBicicletas.Modelo.Item import Item
class Usuario:
    def __init__(self) :




        self.saldo:int = 0
        self.listabicis_en_posecion:{'Item'}={}
        self.Listado_de_Transacciones:list[Transaccion]=[]
        self.contador_transacciones:int = 0

        
    def visualizar_saldo(self):
        return self.saldo

    def bicicletas_en_posecion(self):
        for i in self.listabicis_en_posecion.values():
            print(i)



    def aumentar_saldo(self,saldo_aumentar):
        self.saldo += saldo_aumentar

    def cargar_bicicleta(self,id_dado,bicicleta):
        self.listabicis_en_posecion[id_dado] = bicicleta



