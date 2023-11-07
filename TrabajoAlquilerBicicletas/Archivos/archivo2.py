import pickle
data ={}

with open("archivo_bicicletas", "wb") as archivo:
    pickle.dump(data, archivo)