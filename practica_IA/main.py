import os
from src import carga as c

base = os.path.dirname(os.path.abspath(__file__))
ruta = os.path.join(base, "datos", "sensores.csv")

ids, sensores = c.cargaCSV(ruta)
