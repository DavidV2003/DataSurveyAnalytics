#Importar librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#Importar clases con las funciones para graficar y limpiar respectivamente
from graficos import *
from limpieza import *

#Importar el Csv a un DataFrame
df_o = pd.read_csv('base de datos gto google - Sheet.csv',sep=",")

#Guardar ambas clases en variables para su uso
graficos=graficos()
limpieza=limpieza()

#Crear la carpeta Resultados
limpieza.crear_carpeta_resultados()

#Esta funcion elimina el doble index
df_f=limpieza.combinar_index(df_o)

#Esta funcion toma cada pregunta y hace un conteo de las respuesta y separa los resultados en csv guardados en la carpeta Resultados
limpieza.count(df_f)

#Guarda un indice de las preguntas para saber de cual se habla
limpieza.preguntas(df_o, 'preguntas.xlsx')

#Genera los graficos con las preguntas que se le inserten
#limpieza.crear_carpeta_graficos()
#graficos.grafico_pie([1,2,3])

#Montar un Dash
carpeta='Resultados/'
graficos.dashboard(carpeta)