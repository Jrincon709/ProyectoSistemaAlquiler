import pickle
from TrabajoAlquilerBicicletas.Modelo.Bicicleta import Bicicleta
from collections import OrderedDict
# Datos a guardar en el archivo .pickle
data = OrderedDict({
    13: Bicicleta(13, "BMX", "Rojo", 100000),
    14: Bicicleta(14, "BMX", "Gris", 100000),
    15: Bicicleta(15, "BMX", "Rojo", 100000),
    16: Bicicleta(16, "BMX", "Gris", 100000),
    20: Bicicleta(20, "Montana","Verde", 150000),
    21: Bicicleta(21, "Montana", "Naranja", 150000),
    22: Bicicleta(22, "Montana", "Negro", 150000),
    34: Bicicleta(34,"Hibrida", "Rosa", 80000),
    35: Bicicleta(35, "Hibrida", "Verde", 80000),
    36: Bicicleta(36, "Hibrida", "Rojo", 80000),
    37: Bicicleta(37, "Hibrida", "Blanca", 80000),
    42: Bicicleta(42, "Triatlon","Naranja", 200000),
    43: Bicicleta(43, "Triatlon","Lila", 200000),
    44: Bicicleta(44, "Triatlon", "Gris", 200000),
    45: Bicicleta(45, "Triatlon", "Cafe", 200000),
    46: Bicicleta(46 ,"Plegable", "Azul", 200000),
    47: Bicicleta(47 ,"Plegable", "Salmon", 200000),
})

with open("archivo_pickle", "wb") as archivo:
    pickle.dump(data, archivo)


