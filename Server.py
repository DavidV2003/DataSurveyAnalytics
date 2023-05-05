
import dash
from dash import dcc
from dash import html
import glob
import os
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from sklearn.linear_model import LinearRegression

# Definir la carpeta que contiene los archivos CSV
carpeta = 'Resultados/'

# Leer los archivos CSV y guardarlos en un diccionario
archivos = {}
for archivo in glob.glob(os.path.join(carpeta, '*.csv')):
    nombre = os.path.splitext(os.path.basename(archivo))[0]
    df = pd.read_csv(archivo)
    archivos[nombre] = df

# Ordenar los nombres de los archivos alfabéticamente
nombres_ordenados = sorted(list(archivos.keys()))

# Crear las diferentes gráficas
graficas = {}
for nombre, df in archivos.items():
    grafica = px.line(df, y='Conteo', x=nombre)
    graficas[nombre] = grafica

# Crear la aplicación de Dash
app = dash.Dash(__name__)

# Crear el diseño de la interfaz de usuario
# Crear el diseño de la interfaz de usuario
app.layout = html.Div([
    html.H1('Dashboard'),
    dcc.Dropdown(
        id='selector-archivo',
        options=[{'label': str(i), 'value': str(i)} for i in range(1, len(archivos)+1)],
        value=nombres_ordenados[0]
    ),
    dcc.Graph(id='grafica'),
    dcc.Graph(id='grafica2'),
    dcc.Graph(id='grafica3'),
    dcc.Graph(id='grafica4'),
    dcc.Graph(id='grafica5'),
    dcc.Graph(id='grafica6')
])

# Definir la función de actualización de la gráfica
@app.callback(Output('grafica', 'figure'),
              Input('selector-archivo', 'value'))
def actualizar_grafica(nombre_archivo):
    return graficas[nombre_archivo]

# Definir la función de actualización de la segunda gráfica
@app.callback(Output('grafica2', 'figure'),
              Input('selector-archivo', 'value'))
def actualizar_grafica2(nombre_archivo):
    df = archivos[nombre_archivo]
    grafica = px.bar(df, y='Conteo', x=str(nombre_archivo))
    return grafica

# Definir la función de actualización de la tercera gráfica
@app.callback(Output('grafica3', 'figure'),
              Input('selector-archivo', 'value'))
def actualizar_grafica3(nombre_archivo):
    df = archivos[nombre_archivo]
    grafica = px.scatter(df, y='Conteo', x=str(nombre_archivo))
    return grafica

# Definir la función de actualización de la cuarta gráfica
@app.callback(Output('grafica4', 'figure'),
              Input('selector-archivo', 'value'))
def actualizar_grafica4(nombre_archivo):
    df = archivos[nombre_archivo]
    grafica = px.bar(df, y='Conteo', x=str(nombre_archivo), barmode='stack')
    return grafica

# Definir la función de actualización de la quinta gráfica
@app.callback(Output('grafica5', 'figure'),
              Input('selector-archivo', 'value'))
def actualizar_grafica5(nombre_archivo):
    df = archivos[nombre_archivo]
    grafica = px.pie(df, values=str(nombre_archivo), names='Conteo')
    return grafica

# Definir la función de actualización de la sexta gráfica
@app.callback(Output('grafica6', 'figure'),
              Input('selector-archivo', 'value'))
def actualizar_grafica6(nombre_archivo):
    df = archivos[nombre_archivo]
    grafica = px.area(df, y='Conteo', x=str(nombre_archivo))
    return grafica

# Ejecutar la aplicación de Dash
if __name__ == '__main__':
    app.run_server(debug=True)