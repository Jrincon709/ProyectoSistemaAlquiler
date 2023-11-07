import tkinter as tk
from tkinter import ttk, messagebox

from TrabajoAlquilerBicicletas.View.Interfaz.InicioSesion import Tienda

class MostrarCatalogo:
    def __init__(self):
        self.tiendita = Tienda()





        self.catalogo = self.tiendita.cargar_catalogo()

        self.ventana = tk.Tk()
        self.ventana.title ("Catálogo de Bicicletas")
        self.ventana.geometry ("800x550")

        titulo_label = tk.Label (self.ventana, text="Catálogo de bicicletas disponibles",
                                 font=("Cascadia Code ExtraLight", 20), bg='#FFD1DC')
        titulo_label.pack (pady=10)

        self.lista_bicicletas = tk.Listbox (self.ventana, font=("Cascadia Code ExtraLight", 15))
        self.lista_bicicletas.pack (expand=True, fill="both")

        for id, bicicleta in self.catalogo.items ():
            self.lista_bicicletas.insert (tk.END, bicicleta)

        self.mostrar()

    def mostrar(self):
        self.ventana.mainloop ()

