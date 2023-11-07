
import tkinter as tk

from TrabajoAlquilerBicicletas.Modelo.Tienda import Tienda
from TrabajoAlquilerBicicletas.View.consola import UIConsola




class VentanaMenuPrincipal(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.Consola =UIConsola()
        self.title("Menu")
        self.tiendita = Tienda ()
        self.geometry ('600x500')
        self.config (bg='#FFFFFF')