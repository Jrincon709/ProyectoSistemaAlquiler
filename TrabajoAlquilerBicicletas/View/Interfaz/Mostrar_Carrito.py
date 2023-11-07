
import tkinter as tk

from TrabajoAlquilerBicicletas.Modelo.Tienda import Tienda


class MostrarCarritodeCompras:
    def __init__(self):

        self.tiendita = Tienda()




        print (self.tiendita.carro_compras.items)

        self.ventana = tk.Tk()
        self.ventana.title ("Carrito de Compras")
        self.ventana.geometry ("800x550")

        # Crear un Text widget para mostrar el carrito

        titulo_label = tk.Label (self.ventana, text="El contenido de tu carro de compras",
                                 font=("Cascadia Code ExtraLight", 20), bg='#FFD1DC')
        titulo_label.pack (pady=10)

        self.texto_carrito = tk.Listbox(self.ventana, font=("Cascadia Code ExtraLight", 15))
        self.texto_carrito.pack(expand=True, fill="both")

        # Iterar sobre el carrito de compras y mostrarlo en el Text widget
        for item in self.tiendita.carro_compras.items:
            item_str = str (item)
            self.texto_carrito.insert (tk.END, item_str)
        # Reemplaza 'item.descripcion' con el atributo correcto

        self.mostrar()

    def mostrar(self):
        self.ventana.mainloop ()