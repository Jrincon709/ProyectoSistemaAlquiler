import json
import pickle
from TrabajoAlquilerBicicletas.Modelo.Item import Item
from TrabajoAlquilerBicicletas.Modelo.Bicicleta_No_En_Posecion import Bicicleta_No_En_Posecion
from  TrabajoAlquilerBicicletas.Modelo.Carrito_Compras import Carrito_compras
from TrabajoAlquilerBicicletas.Modelo.Bicicleta import Bicicleta
from TrabajoAlquilerBicicletas.Modelo.BicicletaExistenteError import BicicletaExistenteError
from TrabajoAlquilerBicicletas.Modelo.Bicicleta_NoDisponible_Error import BicicletaNoDisponibleError
from TrabajoAlquilerBicicletas.Modelo.Transacciones import Transaccion
from TrabajoAlquilerBicicletas.Modelo.Usuario import Usuario
from TrabajoAlquilerBicicletas.Modelo.Saldo_Insuficiente_Error import Saldo_Insuficiente_Error
from TrabajoAlquilerBicicletas.Modelo.NumerosNegativosError import NumerosNegativosError
import os

directorio_actual = os.path.dirname(os.path.realpath(__file__))
archivo_pickle = os.path.join(directorio_actual,"../Archivos/archivo_pickle")
Usuarios_json = os.path.join(directorio_actual,"../Archivos/Usuarios.json")
bicicletas_pickle = os.path.join(directorio_actual,"../Archivos/archivo_bicicletas")

class Tienda:
    def __init__(self):
        self.listausuarios: dict = {}
        self.Catalogo_Bicicletas:dict = {}
        self.carro_compras = Carrito_compras()
        self.plata_tienda = 0
        self.servicio_usuario = Usuario()
        self.lista_bicis_enespera= {}
        self.cargar_usuarios()
        self.bicicletas_por_usuario = {}
        self.cargar_datos_bicicletas()
        self.usuario_actual = None



    def cargar_usuarios(self):
        try:
            # Carga la lista de usuarios desde un archivo (si existe)
            with open(Usuarios_json, 'r') as file:
                self.listausuarios = json.load(file)
        except FileNotFoundError:
            # Si el archivo no existe, crea un diccionario vacío
            self.listausuarios = {}


    def registrar(self, usuario, paswoord):
        if usuario in self.listausuarios:
            return "El nombre de usuario ya esta en uso"
        else:
            self.listausuarios[usuario] = paswoord
            self.guardar_usuarios()
            return "Usuario registrado con exito"



    def autenticar(self, usuario, paswoord):
        self.cargar_usuarios()

        if usuario in self.listausuarios and paswoord == self.listausuarios[usuario]:
            self.agregar_bicicleta_a_usuario()
            self.usuario_actual = usuario
            return True
        else:
            return False


    def guardar_usuarios(self):
        # Guarda el diccionario de usuarios en un archivo
        with open(Usuarios_json, 'w') as file:
            json.dump(self.listausuarios, file)




    def guardar_bicicletas_por_usuario(self):

        with open(bicicletas_pickle,"wb") as archivo:
            pickle.dump(self.bicicletas_por_usuario, archivo)


    def cargar_datos_bicicletas(self):
        try:
            # Carga el diccionario de usuarios desde un archivo (si existe)
            with open (bicicletas_pickle, 'rb') as archivo:
                self.bicicletas_por_usuario = pickle.load (archivo)

        except FileNotFoundError:
            self.bicicletas_por_usuario = {}

    def eliminarbicidedict(self):
        usuario = self.obtenerusuario()
        if usuario in self.bicicletas_por_usuario.keys():
            del self.bicicletas_por_usuario[usuario]
        self.guardar_bicicletas_por_usuario()

    def agregar_bicicleta_a_usuario(self):
        self.cargar_datos_bicicletas()
        usuario = self.obtenerusuario()
        if usuario in self.bicicletas_por_usuario.keys():
            diccionario_bicicletas = self.bicicletas_por_usuario[usuario]
            self.servicio_usuario.listabicis_en_posecion.update (diccionario_bicicletas)

        self.guardar_bicicletas_por_usuario ()




    def obtenerusuario(self):
        return self.usuario_actual

    def mostrar_catalogo(self):
        self.cargar_catalogo()
        for bicicleta in self.Catalogo_Bicicletas.values ():
            print (bicicleta)








    def cargar_catalogo(self):
        with open (archivo_pickle, "rb") as archivo:
            self.Catalogo_Bicicletas = pickle.load(archivo)
        return self.Catalogo_Bicicletas

    def guardar_catalogo(self):

        with open(archivo_pickle,"wb") as archivo:
            pickle.dump(self.Catalogo_Bicicletas, archivo)

#Verifica si la  bicicleta esta en el catalodo
    def verificar_bicicleta_en_catalogo(self,id_pedido):
        if id_pedido not in self.Catalogo_Bicicletas.keys():
            raise BicicletaExistenteError(id_pedido)
        #verifica si hay bicicletas en el carro de compras

    def verificar_bicicleta_en_carrito(self,id_pedido):
        for item in self.carro_compras.items:
            if item.bicicleta.id == id_pedido:
                return  item.bicicleta
        raise BicicletaNoDisponibleError (id_pedido)



#adiciona las bicicletas alquiladas al catalogo
    def adicionar_bicicleta_catalogo(self, id_pedido:int , bicicleta:Bicicleta):
         if id_pedido not in self.Catalogo_Bicicletas.keys():
             self.Catalogo_Bicicletas[id_pedido]= bicicleta

#crea un item de la bicicleta y las horas y las agrega al carro de compras
    def agregar_bici_a_carrito(self, bicicleta: Bicicleta, horas:int):

        return self.carro_compras.agregar_item(bicicleta, horas)
# retira el item del carrito de compras
    def retirar_item_de_carrito(self, id_pedido:int):
        self.carro_compras.quitar_item(id_pedido)

#cuando la bicicleta se compra se retira del carro de compras
    def retirar_item_comprado_de_bicicleta(self):
        for i in self.carro_compras.items:
            self.carro_compras.quitar_item(i.bicicleta.id)




    def procesar_pago(self):
        saldo = self.servicio_usuario.saldo
        total_carrito = self.carro_compras.calcular_costo_total()
        if saldo == 0 or saldo - total_carrito < 0:
            raise Saldo_Insuficiente_Error(saldo,total_carrito)
        else:
            self.servicio_usuario.saldo -= total_carrito
            self.plata_tienda += total_carrito

            self.quitar_bicicletacomprada_de_lista_en_espera()
            self.agregar_bicicletas_a_diccionario()



#se quita la bicicleta del catalogo y se añade a un diccionario de lista bicicletas en espera
    #clave el id y valor la bicicleta
    def bicicletas_en_espera_de_compra(self,id):

        bicicleta_de_carrito = self.Catalogo_Bicicletas.pop(id)
        self.lista_bicis_enespera[id] = bicicleta_de_carrito


#se hace una lista de los id de la bicicleta y eliminamos las bicis de la lista bicis en espera y se llama el metodo adicionar_bicicleta_al_ususario
    def quitar_bicicletacomprada_de_lista_en_espera(self):
        listade_idbicis_enespera = list(self.lista_bicis_enespera.keys())
        for i in listade_idbicis_enespera:
            bicicleta_comprada = self.lista_bicis_enespera.pop(i)
            self.adicionar_bicicleta_al_ususario(i,bicicleta_comprada)

#recibe id y bicicleta y se añade la bicicleta al diccionario lista bicis en posicion
    def adicionar_bicicleta_al_ususario(self,id_dado,bicicleta):
        self.servicio_usuario.listabicis_en_posecion[id_dado] = bicicleta

    def agregar_bicicletas_a_diccionario(self):
        usuario = self.obtenerusuario ()
        if usuario in self.bicicletas_por_usuario:
            diccionario_bicicletas = self.servicio_usuario.listabicis_en_posecion
            self.bicicletas_por_usuario.update (diccionario_bicicletas)

        else:

            self.bicicletas_por_usuario[usuario] = self.servicio_usuario.listabicis_en_posecion

        self.guardar_bicicletas_por_usuario ()







    def devolver_bicicleta(self, id_pedido:int):
        if id_pedido in self.servicio_usuario.listabicis_en_posecion.keys():
            bicicleta_a_devolver = self.servicio_usuario.listabicis_en_posecion.pop (id_pedido)
            self.adicionar_bicicleta_catalogo (id_pedido, bicicleta_a_devolver)
            self.eliminarbicidedict()
            self.guardar_bicicletas_por_usuario()
        else:
            raise Bicicleta_No_En_Posecion(id_pedido)





    def adicionar_transaccion(self,fecha,valor_total):

        bicicletas_alquiladas = []

        for item in self.carro_compras.items:
            bicicletas_alquiladas.append(item.bicicleta)

        #retiramos el item(bicicleta, valor_hora) del carro de compras
        self.retirar_item_comprado_de_bicicleta ()

        if bicicletas_alquiladas:
            nueva_transaccion = Transaccion (self.servicio_usuario.contador_transacciones,bicicletas_alquiladas,fecha,valor_total)
            self.servicio_usuario.Listado_de_Transacciones.append( nueva_transaccion)
            self.servicio_usuario.contador_transacciones += 1


    def ver_transacciones(self):
        for transaccion in self.servicio_usuario.Listado_de_Transacciones:
            print (transaccion)





