import tkinter as tk
from tkinter import messagebox

from TrabajoAlquilerBicicletas.Modelo.Tienda import Tienda


class VentanaRegistro(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Registro de Usuario")
        self.tiendita = Tienda()
        self.usuario = tk.StringVar ()
        self.paswoord = tk.StringVar ()


        self.geometry ('600x500')
        self.config (bg='#FFFFFF')

        #texto de registro
        frame_mensaje = tk.Frame (self, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_mensaje.pack (side="top", expand=tk.YES, fill=tk.BOTH)

        Label_MensajeBienvenida = tk.Label (frame_mensaje, text="Registrar usuario",
                                            font=("Cascadia Code ExtraLight", 16), bg='#FFD1DC')
        Label_MensajeBienvenida.pack (pady=20)

        # Widgets para ingresar usuario y contraseña
        label_usuario = tk.Label (self, text="Usuario:", bg='#FFD1DC', font=("Cascadia Code ExtraLight", 10))
        entry_usuario = tk.Entry (self, textvariable=self.usuario)
        label_paswoord = tk.Label (self, text="Contraseña:",bg='#FFD1DC', font=("Cascadia Code ExtraLight", 10))
        entry_paswoord = tk.Entry (self, textvariable=self.paswoord, show='*')

        btn_guardar = tk.Button (self, text="Guardar Registro", command=self.guardar_registro ,bg='#FFD1DC',font=("Cascadia Code ExtraLight", 10))

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

    def guardar_registro(self):
        usuario = self.usuario.get ()
        paswoord = self.paswoord.get ()
        nuevo_usuario = self.tiendita.registrar (usuario, paswoord)

            # Mostrar un mensaje emergente con el resultado
        messagebox.showinfo ("Resultado", nuevo_usuario)