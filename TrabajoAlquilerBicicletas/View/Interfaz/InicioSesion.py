



import tkinter as tk
from tkinter import messagebox

from TrabajoAlquilerBicicletas.Modelo.Tienda import Tienda
from TrabajoAlquilerBicicletas.View.Interfaz.PanelMaestro import MasterPanel


class VentanaIniciarSesion(tk.Toplevel):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.title("Iniciar Sesion")
        self.tiendita = Tienda()

        self.usuario = tk.StringVar ()
        self.paswoord = tk.StringVar ()
        self.raiz = raiz

        self.geometry ('600x500')
        self.config (bg='#FFFFFF')

        # texto de registro
        frame_mensaje = tk.Frame (self, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_mensaje.pack (side="top", expand=tk.YES, fill=tk.BOTH)

        Label_MensajeBienvenida = tk.Label (frame_mensaje, text="Iniciar Sesion",
                                            font=("Cascadia Code ExtraLight", 16), bg='#FFD1DC')
        Label_MensajeBienvenida.pack (pady=20)

        # Widgets para ingresar usuario y contraseña
        label_usuario = tk.Label (self, text="Usuario:", bg='#FFD1DC', font=("Cascadia Code ExtraLight", 10))
        entry_usuario = tk.Entry (self, textvariable=self.usuario)
        label_paswoord = tk.Label (self, text="Contraseña:", bg='#FFD1DC', font=("Cascadia Code ExtraLight", 10))
        entry_paswoord = tk.Entry (self, textvariable=self.paswoord, show='*')

        btn_guardar = tk.Button (self, text="Iniciar Sesion", command=self.autentifica_usuario, bg='#FFD1DC',
                                 font=("Cascadia Code ExtraLight", 10))

        # Colocar los widgets en la ventana
        label_usuario.pack (side="top")

        entry_usuario.pack (side="top")

        label_paswoord.pack (side="top")
        entry_paswoord.pack (side="top")
        btn_guardar.pack (side="top")

        label_usuario.place (relx=0.3, rely=0.3, anchor="center")
        entry_usuario.place (relx=0.7, rely=0.3, anchor="center")
        label_paswoord.place (relx=0.3, rely=0.5, anchor="center")
        entry_paswoord.place (relx=0.7, rely=0.5, anchor="center")
        btn_guardar.place (relx=0.5, rely=0.7, anchor="center")


    def autentifica_usuario(self):
        usuario = self.usuario.get ()
        paswoord = self.paswoord.get ()
        resultado =self.tiendita.autenticar (usuario, paswoord)

        if resultado:
            resultado = f"Ingreso de Sesion realizado con exito, Bienvenid@ {usuario}."
            messagebox.showinfo ("Resultado", resultado)
            self.destroy ()  # Cierra la ventana actual
            MasterPanel()  # Abre la siguiente ventana
        else:
            resultado = "Nombre de usuario o contraseña incorrectos. Por favor, intente nuevamente."
            messagebox.showinfo ("Resultado", resultado)

