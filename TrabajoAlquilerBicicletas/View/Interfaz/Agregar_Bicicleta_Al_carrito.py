


import tkinter as tk
from tkinter import messagebox, ttk
from TrabajoAlquilerBicicletas.Modelo.BicicletaExistenteError import BicicletaExistenteError
from TrabajoAlquilerBicicletas.Modelo.Tienda import Tienda
class AgregarBicicletaACarrito:
    def __init__(self):
        self.tiendita = Tienda()

        self.ventana = tk.Tk()





        self.tiendita.cargar_catalogo ()

        self.ventana.title ("Agregar Bicicleta al Carrito")
        self.ventana.geometry ("400x550")


        label_id = tk.Label(self.ventana, text="Ingresa el ID de la Bicicleta:", font=("Cascadia Code ExtraLight", 12))
        label_id.pack()

        self.id = ttk.Entry(self.ventana, font=('Times', 14))
        self.id.pack()

        label_cantidad = tk.Label(self.ventana, text="Ingresa la cantidad de horas:", font=("Cascadia Code ExtraLight", 12))
        label_cantidad.pack()

        self.cantidad = ttk.Entry(self.ventana, font=('Times', 14))
        self.cantidad.pack()

        btn_agregar = tk.Button(self.ventana, text="Agregar al Carrito", font=("Cascadia Code ExtraLight", 12),
                                command=self.agregar_al_carrito)
        btn_agregar.pack()


        self.ventana.mainloop ()

    def agregar_al_carrito(self):

        try:

            id_producto = int (self.id.get())
            cantidad = int (self.cantidad.get ())
                # Verificar la disponibilidad de la bicicleta en el catálogo
            self.tiendita.verificar_bicicleta_en_catalogo (id_producto)
            bicicleta = self.tiendita.Catalogo_Bicicletas[id_producto]

            # Agregar la bicicleta al carrito
            self.tiendita.agregar_bici_a_carrito (bicicleta, cantidad)
            self.tiendita.bicicletas_en_espera_de_compra (id_producto)
            mensaje = f"Has agregado por {cantidad} horas, bicicleta(s) : {bicicleta} al carrito con exito "
            messagebox.showinfo ("Resultado", mensaje)
            print(self.tiendita.carro_compras.items)





        except ValueError:
            messagebox.showerror ("Error", "Por favor, ingrese valores enteros válidos para ID y Cantidad.")

        except BicicletaExistenteError as e:
            messagebox.showerror ("Error", str (e))

