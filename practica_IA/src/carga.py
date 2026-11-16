#Clase que se encarga de todo lo relacionado con la carga y exploración inicial de datos
import numpy as np

#Carga el fichero csv
def cargaCSV(ruta):
    ids = np.loadtxt(ruta, delimiter=",", skiprows=1, usecols=0, dtype=str)
    datos = np.loadtxt(ruta, delimiter=",", skiprows=1, usecols=(1, 2, 3, 4, 5))
    return ids, datos

def exploracionDatos(csvLeido):
    #Numero de dimensiones del fichero
    print(csvLeido.ndim)


#Añadir funcion para imprimir por pantalla bonito