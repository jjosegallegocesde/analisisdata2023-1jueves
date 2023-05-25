import pandas as pd
from data.data1 import apartamento1,apartamento2
from helpers.crearTablasHTML import crearTabla

tabla1=pd.DataFrame(apartamento1,columns=['edad'])
tabla2=pd.DataFrame(apartamento2,columns=['edad'])
tabla3=pd.read_csv("./data/empleados.csv")

#FILTRANDO O APLICANDO CONDICIONES A MI DATAFRAME
analistas1=tabla3.query('cargo=="analista1"')
analistas2=tabla3.query('cargo=="analista2"')
jubilados=tabla3.query('edad>=50')

#Generemos las tablas para el reporte
crearTabla(analistas1,"analistas1")
crearTabla(analistas2,"analistas2")
crearTabla(jubilados,"jubilados")


