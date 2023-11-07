import sys
from TrabajoAlquilerBicicletas.Modelo.Bicicleta import Bicicleta
from TrabajoAlquilerBicicletas.Modelo.BicicletaExistenteError import BicicletaExistenteError
from TrabajoAlquilerBicicletas.Modelo.Bicicleta_NoDisponible_Error import BicicletaNoDisponibleError
from TrabajoAlquilerBicicletas.Modelo.Saldo_Insuficiente_Error import Saldo_Insuficiente_Error
from TrabajoAlquilerBicicletas.Modelo.Bicicleta_No_En_Posecion import Bicicleta_No_En_Posecion
from TrabajoAlquilerBicicletas.Modelo.Tienda import Tienda
import datetime
from TrabajoAlquilerBicicletas.Modelo.NumerosNegativosError import NumerosNegativosError


class UIConsola:

    def __init__(self) -> None:
        self.sesion_iniciada:bool = False
        self.sistema_tienda = Tienda()
        self.sistema_tienda.cargar_catalogo()
        self.sistema_tienda.cargar_usuarios()


    @staticmethod
    def mostrar_menu():
        print("====================================================")
        print("  Bienvenido a la tienda de alquiler de bicicletas  ")
        print("====================================================")

    def mostrar_menu_principal_noinisiado (self):
        self.mostrar_menu()
        print("\nOpciones:")
        print("1. Iniciar Sesión")
        print("2. Registrar Usuario")
        print("3. Salir")
        opcion = int(input("Ingrese una opción: "))
        return opcion

    def mostrar_menu_principal_inisiado(self):
        self.mostrar_menu()
        print("\nOpciones:")
        print("1. Ver catálogo de bicicletas")
        print("2. Ver carrito de compras")
        print("3. Visualizar Saldo")
        print("4. Agregar Bicicleta al Carrito de Compras")
        print("5. Eliminar Bicicleta del Carrito de Compras")
        print("6. Pagar Carrito de Compras")
        print("7. Ver Bicicletas Alquiladas")
        print("8. Devolver Bicicletas")
        print("9. Ver Tu historial de Transacciones")
        print("10. Cerrar Sesión")
        print("11. Salir")

        

     
    def ejecutar (self):
        while True:
            if self.sesion_iniciada:

                self.mostrar_menu_principal_inisiado()
                opciones = {
                    "1": self.ver_catalago_bicicletas,
                    "2": self.carro_compras,
                    "3": self.recargar_saldo,
                    "4": self.agregar_bicicleta_a_carrito,
                    "5": self.eliminar_bicicleta_de_carrito,
                    "6": self.pagar_carrito,
                    "7": self.visualizar_bicicletas,
                    "8": self.devolver_bicicleta_al_catalogo,
                    "9": self.ver_historial_de_transacciones,
                    "10": self.cerrarsesion,
                    "11": self.salir
                }

                opcion = input ("Seleccione una opción: ")
                accion = opciones.get (opcion)
                if accion:
                    accion ()
                else:
                    print (f"{opcion} no es una opción válida")



            else:
                try:
                    opcion = self.mostrar_menu_principal_noinisiado()
                    if opcion == 1:
                        self.iniciar_sesion()
                    elif opcion == 2:
                        self.registrar_usuario()
                    elif opcion == 3:
                        self.salir()
                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida.")
                except ValueError:
                    print ("Entrada no válida. Por favor, ingrese un número válido.")



    def registrar_usuario(self):
        print("----------------------------------------------------------------------------------------------------")
        print("================")
        print("Registar Usuario")
        print("================")
        print("\n")

        usuario = (input ("Ingrese un usuario :"))
        paswoord = input ("Ingrese una contraseña:")
        resultado = self.sistema_tienda.registrar( usuario, paswoord)
        print(resultado)





    def iniciar_sesion (self):
        print("----------------------------------------------------------------------------------------------------")
        print("================")
        print(" Iniciar sesion ")
        print("================")
        print("\n")

        u_ingresado =  (input ("Ingrese el usuario registrado :"))
        paswoord = input("Ingrese la contraseña:")

        if self.sistema_tienda.autenticar(u_ingresado,paswoord):
            print (f"Bienvinido a nuestra tienda, usuario {u_ingresado}")
            self.sistema_tienda.agregar_bicicleta_a_usuario()
            self.sesion_iniciada =True



        else:
            print("Nombre de usuario o contraseña incorrectos. Por favor, intente nuevamente.")




    @staticmethod
    def salir():
        print("==============================================================")
        print("  === Gracias Por Usar Nuestro Servicios, Vuelva Pronto ===   ")
        print("==============================================================")
        sys.exit(0)

    def ver_catalago_bicicletas(self):
        print("----------------------------------------------------------------------------------------------------")
 
        print("======================")
        print("Catalago de Bicicletas")
        print("======================")
        print("\n")

        self.sistema_tienda.mostrar_catalogo()

    def agregar_bicicleta_a_carrito(self):
        print("----------------------------------------------------------------------------------------------------")
        print("===================================")
        print("    Agregar Bicicleta Al Carrito   ")
        print("===================================")
        print("\n")

        while True:
            try:
                id_pedido = int(input ("Por favor ingrese el ID de la bicicleta a agregar al carrito: "))
                print ("Por favor ingrese la cantidad de horas que deseas "
                       "alquilar la bicicleta ")
                self.sistema_tienda.verificar_bicicleta_en_catalogo (id_pedido)
                cantidad = self.Numeros_Negativos()

            except BicicletaExistenteError as err:
                print (err)
            except ValueError:
                print ("Por favor ingrese un número valido")
            else:
                bicicleta = self.sistema_tienda.Catalogo_Bicicletas[id_pedido]

                self.sistema_tienda.agregar_bici_a_carrito(bicicleta, cantidad)
                self.sistema_tienda.bicicletas_en_espera_de_compra(id_pedido)
                print ("Bicicleta agregada al carrito.")
                self.sistema_tienda.guardar_catalogo()
                break


    def carro_compras(self):
        print("----------------------------------------------------------------------------------------------------")
  
        print("===================")
        print("Carrito de Compras")
        print("===================")
        print("\n")

        print("Este es el contenido de tu carro de compras :")
        self.sistema_tienda.carro_compras.mostrar_carrito()
        costo_total = self.sistema_tienda.carro_compras.calcular_costo_total ()
        print (f"El costo total de tu carrito es : {costo_total}")





    def cerrarsesion(self):
        print("----------------------------------------------------------------------------------------------------")
        print("=======================================")
        print("  === Hasta Luego, ¡Vuelva Pronto! === ")
        print("=======================================")
        self.sesion_iniciada = False


    def recargar_saldo(self):
        print ("----------------------------------------------------------------------------------------------------")
        print ("===================")
        print ("        Saldo      ")
        print ("===================")
        print ("\n")
        saldo_actual = self.sistema_tienda.servicio_usuario.visualizar_saldo()
        print (f"Tu saldo actual es : {saldo_actual}")
        print ("\nOPCIONES:")
        print ("1. Recargar saldo")
        print ("2. Regresar al menu")

        while True:
            try:
                valor = int (input ("Ingresa la opcion que deseas:  "))
                if valor == 1:
                    print("¿Cuanto saldo deseas agregar")

                    saldo = self.Numeros_Negativos()

                    self.sistema_tienda.servicio_usuario.aumentar_saldo(saldo)
                    print ("Saldo actualizado con exito")


            except ValueError:
                print ("Por favor ingrese un número valido")
            else:
                break




    def pagar_carrito(self):
        print ("----------------------------------------------------------------------------------------------------")
        print ("===================")
        print (" Pagar Carrito     ")
        print ("===================")
        print("\n")
        saldo_actual = self.sistema_tienda.servicio_usuario.visualizar_saldo()
        costo_total= self.sistema_tienda.carro_compras.calcular_costo_total()
        print (f"Tu saldo actual es : {saldo_actual}")
        print(f"El Valor total de los productos en tu carrito es de: {costo_total}")
        print ("\nOPCIONES:")
        print ("1. Pagar Carrito")
        print ("2. Regresar al menu")
        while True:
            try:
                valor = int (input ("Ingresa la opcion que deseas:  "))
                if valor == 1:
                    self.sistema_tienda.procesar_pago()
                    self.transacciones(costo_total)
                    self.sistema_tienda.guardar_catalogo()
                    print (f"Realizaste el pedido con un valor de {costo_total} con exito")
                    print(f"Disfruta tu bicicleta")

            except ValueError:
                print ("Por favor ingrese un número valido  ")
            except Saldo_Insuficiente_Error as err:
                print (err)
            else:
                break


    def Numeros_Negativos(self,):
        while True:
            try:
                numero = int (input ("Ingresa el valor a agreagar: "))
                NumerosNegativosError.validar_numero_negativo (numero)

            except NumerosNegativosError as err:
                print (f"Error: {err}")
            else:
                return numero


    def transacciones(self,valor_total):
        while True:
            try:
                fecha_str = input ("Ingresa una fecha (YYYY-MM-DD): ")
                fecha = datetime.datetime.strptime (fecha_str, "%Y-%m-%d")
                self.sistema_tienda.adicionar_transaccion (fecha,valor_total)
            except ValueError:
                print("El Formato de fecha esta incorrecto. Debe ser 'YYYY-MM-DD'.")

            else:
                break


    def visualizar_bicicletas(self):
        print ("----------------------------------------------------------------------------------------------------")
        print ("===================================")
        print (" Bicicletas En tu Disposicion     ")
        print ("==================================")
        print ("\n")
        print("Estas son las bicicletas que tienes alquiladas:")
        self.sistema_tienda.servicio_usuario.bicicletas_en_posecion()


    def devolver_bicicleta_al_catalogo(self):
        print ("----------------------------------------------------------------------------------------------------")
        print ("===================================")
        print ("    Devolver Bicicletas            ")
        print ("==================================")
        print ("\n")
        print ("\nOPCIONES:")
        print ("1. Devolver bicicleta")
        print ("2. Regresar al menu")
        while True:
            try:
                valor = int (input ("Ingresa la opcion que deseas:  "))
                if valor == 1:

                    id_pedido = int (input ("Por favor ingrese el ID de la bicicleta a devolver: "))
                    self.sistema_tienda.devolver_bicicleta(id_pedido)
                    self.sistema_tienda.guardar_catalogo()
                    print(f"La bicicleta con el ID {id_pedido} fue devuelta con exito")
            except Bicicleta_No_En_Posecion as err:
                print(err)

            except ValueError:
                print ("Por favor ingrese un número valido")
            else:
                break

    def eliminar_bicicleta_de_carrito(self):
        print ("----------------------------------------------------------------------------------------------------")
        print ("==============================")
        print ("  Eliminar Bicicleta del Carrito")
        print ("==============================")
        print ("\n")
        print ("\nOPCIONES:")
        print ("1. Eliminar Bicicleta del Carrito")
        print ("2. Regresar al menu")

        while True:
            try:
                valor = int (input ("Ingresa la opcion que deseas:  "))
                if valor == 1:

                    id_pedido = int (input ("Por favor ingrese el ID de la bicicleta a eliminar del carrito: "))
                    bici:Bicicleta= self.sistema_tienda.verificar_bicicleta_en_carrito(id_pedido)
                    self.sistema_tienda.retirar_item_de_carrito (id_pedido)
                    self.sistema_tienda.adicionar_bicicleta_catalogo(id_pedido,bici)
                    self.sistema_tienda.guardar_catalogo()

                    print ("Bicicleta eliminada del carrito.")
            except BicicletaNoDisponibleError as err:
                print(err)



            except ValueError:
                print ("Por favor ingrese un número válido.")
            else:
                break

    def ver_historial_de_transacciones(self):
        print ("----------------------------------------------------------------------------------------------------")
        print ("===================")
        print ("Historial de transacciones")
        print ("===================")
        print ("\n")
        self.sistema_tienda.ver_transacciones()

