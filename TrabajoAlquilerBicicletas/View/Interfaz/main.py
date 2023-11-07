import tkinter as tk
from TrabajoAlquilerBicicletas.Modelo.Tienda import Tienda
from TrabajoAlquilerBicicletas.View.Interfaz.Inicial import InicioVentana
from TrabajoAlquilerBicicletas.View.Interfaz.PanelMaestro import MasterPanel

if __name__ == "__main__":
    raiz = tk.Tk()
    app_inicio = InicioVentana(raiz)
    raiz.resizable(0, 0)
    raiz.mainloop()

