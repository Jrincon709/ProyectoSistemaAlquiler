import tkinter as tk

from TrabajoAlquilerBicicletas.View.Interfaz.Agregar_Bicicleta_Al_carrito import AgregarBicicletaACarrito
from TrabajoAlquilerBicicletas.View.Interfaz.Devolver_Bicicletas import DevolverBicicletas
from TrabajoAlquilerBicicletas.View.Interfaz.Eliminar_Bicicleta_del_carritp import EliminarBicicletaAcarrito
from TrabajoAlquilerBicicletas.View.Interfaz.Mostrar_Carrito import MostrarCarritodeCompras
from TrabajoAlquilerBicicletas.View.Interfaz.Mostrar_Catalogo import MostrarCatalogo
from TrabajoAlquilerBicicletas.View.Interfaz.Pagar_Carrito import PagarCarrito
from TrabajoAlquilerBicicletas.View.Interfaz.Ver_Transacciones import VerTransacciones
from TrabajoAlquilerBicicletas.View.Interfaz.Visualizar_Saldo import VisualizarSaldo

class CerrarSesion:
    pass


class MasterPanel:
    def __init__(self):





        self.raiz = tk.Tk()
        self.raiz.title ('Sistema de Alquiler de Bicicletas')
        self.raiz.geometry ('800x600')
        self.raiz.config (bg='#fcfcfc')
        self.raiz.resizable (width=False, height=False)

        frame_mensaje = tk.Frame (self.raiz, bd=0, bg='#fcfcfc')
        frame_mensaje.pack (side="top", expand=tk.YES, fill=tk.BOTH)

        Label_MensajeBienvenida = tk.Label (frame_mensaje, text="Menu Principal", font=("Cascadia Code ExtraLight", 16),
                                            bg='#FFD1DC')
        Label_MensajeBienvenida.pack (pady=20)

        # Botones
        frame_botones = tk.Frame(self.raiz, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_botones.pack(side="bottom", fill="y")

        botones = ["Mostrar Catalogo", "Mostrar Carrito de Compras", "Agregar Bicicleta A Carrito", "Eliminar Bicicleta de Carrito", "Visualizar Saldo",
                   "Procesar Pago", "Devolver las bicicletas en posecion", "Ver Transacciones", "CerrarSesion"]

        # Funciones personalizadas para los botones
        def funcion_boton_1():
            MostrarCatalogo()

        def funcion_boton_2():
            MostrarCarritodeCompras()

        def funcion_boton_3():
            AgregarBicicletaACarrito()

        def funcion_boton_4():
            EliminarBicicletaAcarrito()

        def funcion_boton_5():
            VisualizarSaldo()

        def funcion_boton_6():
            PagarCarrito()

        def funcion_boton_7():
            DevolverBicicletas()

        def funcion_boton_8():
            VerTransacciones()

        def funcion_boton_9():
            CerrarSesion()

        for boton_texto, funcion in zip(botones, [funcion_boton_1, funcion_boton_2, funcion_boton_3, funcion_boton_4,
                                                  funcion_boton_5, funcion_boton_6, funcion_boton_7, funcion_boton_8,
                                                  funcion_boton_9]):
            btn = tk.Button(frame_botones, text=boton_texto, font=("Cascadia Code ExtraLight", 16),
                                            bg='#FFD1DC', bd=0, fg="#000000",
                            command=funcion)
            btn.pack(fill=tk.X, padx=20, pady=10)

        self.raiz.mainloop()