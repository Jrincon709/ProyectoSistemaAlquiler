import tkinter as tk

from TrabajoAlquilerBicicletas.Modelo.Tienda import Tienda
from TrabajoAlquilerBicicletas.View.Interfaz.InicioSesion import VentanaIniciarSesion
from TrabajoAlquilerBicicletas.View.Interfaz.Registro import VentanaRegistro

class InicioVentana(tk.Frame):
    def __init__(self, raiz):

        super ().__init__ (raiz)
        self.tiendita= Tienda()


        self.raiz = raiz
        self.raiz.title("Sistema de Alquiler de Bicicletas")

        self.raiz.geometry ('800x500')
        self.raiz.config (bg='#fcfcfc')

        frame_mensaje = tk.Frame (self.raiz, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_mensaje.pack (side="top", expand=tk.YES, fill=tk.BOTH)

        Label_MensajeBienvenida = tk.Label (frame_mensaje, text="Bienvenido al Sistema de Alquiler de Bicicletas",
                                            font=("Cascadia Code ExtraLight", 16), bg='#FFD1DC')
        Label_MensajeBienvenida.pack (pady=20)

        frame_botones = tk.Frame (self.raiz, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_botones.pack (side="bottom"
                                 "")

        # Botón de inicio de sesión
        btn_iniciar_sesion = tk.Button (frame_botones, text="Iniciar Sesión",
                                        font=('Cascadia Code ExtraLight', 15, "bold"), bg='#FFD1DC',
                                        bd=0, width=20, command=self.abrir_ventana_iniciarsesion)
        btn_iniciar_sesion.pack (fill=tk.X, padx=20, pady=10)

        # Botón de registro de usuario
        btn_registrar_usuario = tk.Button (frame_botones, text="Registrar Usuario",
                                           font=('Cascadia Code ExtraLight', 15, "bold"),
                                           bg='#FFD1DC', bd=0, width=20,
                                           command=self.abrir_ventana_registro)
        btn_registrar_usuario.pack (fill=tk.X, padx=20, pady=10)

        # Botón de Salir

        btn_Salir = tk.Button (frame_botones, text="Salir",
                               font=('Cascadia Code ExtraLight', 15, "bold"),
                               bg='#FFD1DC', bd=0, width=20,
                               command=self.abrir_ventana_salir)
        btn_Salir.pack (fill=tk.X, padx=20, pady=10)



    def abrir_ventana_registro(self):
        ventana_registro = VentanaRegistro (self.raiz)


    def abrir_ventana_iniciarsesion(self):
        ventana_iniciarsesion = VentanaIniciarSesion (self.raiz)



    def abrir_ventana_salir(self):
        pass


