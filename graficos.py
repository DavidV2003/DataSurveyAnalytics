import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class graficos:
    
    def grafico_pie(self, names):
        """
        Crea un gráfico de pastel para cada archivo en la lista 'names'.

        Args:
            names (list): Lista de nombres de archivos (sin extensión) ubicados en la carpeta 'Resultados'.
                        Se espera que cada archivo contenga dos columnas de datos, la primera con los nombres
                        de las etiquetas y la segunda con los valores numéricos.

        Returns:
            None. Los gráficos se guardan en la carpeta 'Graficos' con el mismo nombre que el archivo de origen
            y con la extensión '.png'.

        Raises:
            FileNotFoundError: Si alguno de los archivos de la lista 'names' no se encuentra en la carpeta 'Resultados'.
        """
        for i in range(len(names)):
            try:
                df_g=pd.read_csv(f'Resultados/p{names[i]}.csv',sep=",")
            except FileNotFoundError:
                raise FileNotFoundError(f"El archivo {names[i]}.csv no se encuentra en la carpeta 'Resultados'.")
            columnas = df_g.columns
            # Define la paleta de colores de Seaborn a utilizar.
            colors = sns.color_palette('pastel')[0:5]
            # Crea el gráfico de pastel.
            plt.pie(df_g[columnas[1]][0:5], labels=df_g[columnas[0]][0:5], colors=colors, autopct='%.0f%%')
            plt.savefig(f'Graficos/{names[i]}.png')
            plt.clf()

    def grafico_barras(self, names):
        """
        Crea un gráfico de barras para cada archivo en la lista 'names'.

        Args:
            names (list): Lista de nombres de archivos (sin extensión) ubicados en la carpeta 'Resultados'.
                        Se espera que cada archivo contenga dos columnas de datos, la primera con las etiquetas
                        y la segunda con los valores numéricos.

        Returns:
            None. Los gráficos se guardan en la carpeta 'Graficos' con el mismo nombre que el archivo de origen
            y con la extensión '.png'.

        Raises:
            FileNotFoundError: Si alguno de los archivos de la lista 'names' no se encuentra en la carpeta 'Resultados'.
        """
        for i in range(len(names)):
            try:
                df_g=pd.read_csv(f'Resultados/p{names[i]}.csv',sep=",")
            except FileNotFoundError:
                raise FileNotFoundError(f"El archivo {names[i]}.csv no se encuentra en la carpeta 'Resultados'.")
            columnas = df_g.columns
            # Define la paleta de colores de Seaborn a utilizar.
            colors = sns.color_palette('pastel')[0:5]
            # Crea el gráfico de barras verticales.
            plt.bar(df_g[columnas[0]][0:5], df_g[columnas[1]][0:5], color=colors)
            plt.xlabel(columnas[0])
            plt.ylabel(columnas[1])
            plt.title(names[i])
            plt.savefig(f'Graficos/{names[i]}.png')
            plt.clf()

    def grafico_lineas(self, names):
        """
        Crea un gráfico de líneas para cada archivo en la lista 'names'.

        Args:
            names (list): Lista de nombres de archivos (sin extensión) ubicados en la carpeta 'Resultados'.
                        Se espera que cada archivo contenga dos columnas de datos, la primera con los valores del eje x
                        y la segunda con los valores del eje y.

        Returns:
            None. Los gráficos se guardan en la carpeta 'Graficos' con el mismo nombre que el archivo de origen
            y con la extensión '.png'.

        Raises:
            FileNotFoundError: Si alguno de los archivos de la lista 'names' no se encuentra en la carpeta 'Resultados'.
        """
        for i in range(len(names)):
            try:
                df_g=pd.read_csv(f'Resultados/p{names[i]}.csv',sep=",")
            except FileNotFoundError:
                raise FileNotFoundError(f"El archivo {names[i]}.csv no se encuentra en la carpeta 'Resultados'.")
            columnas = df_g.columns
            # Define la paleta de colores de Seaborn a utilizar.
            colors = sns.color_palette('pastel')[0:5]
            # Crea el gráfico de líneas.
            plt.plot(df_g[columnas[0]][0:5], df_g[columnas[1]][0:5], color=colors[0])
            plt.xlabel(columnas[0])
            plt.ylabel(columnas[1])
            plt.title(names[i])
            plt.savefig(f'Graficos/{names[i]}.png')
            plt.clf()

    def grafico_dispersion(self, names):
        """
        Crea gráficos de dispersión para los archivos .csv con los nombres especificados en la lista names.

        Args:
        - names: lista de strings con los nombres de los archivos .csv a utilizar.

        Returns:
        - None.

        Raises:
        - FileNotFoundError: Si alguno de los archivos CSV no existe.
        """
        for name in names:
            try:
                # Lee el archivo .csv correspondiente.
                df_g = pd.read_csv(f'Resultados/p{name}.csv', sep=",")
            except FileNotFoundError:
                print(f"El archivo Resultados/p{name}.csv no existe.")
                continue
            
            columnas = df_g.columns
            
            # Define la paleta de colores de Seaborn a utilizar.
            colors = sns.color_palette('pastel')[0:5]
            
            # Crea el gráfico de dispersión.
            plt.scatter(df_g[columnas[0]][0:5], df_g[columnas[1]][0:5], color=colors[0])
            
            # Añade las etiquetas de los ejes y el título del gráfico.
            plt.xlabel(columnas[0])
            plt.ylabel(columnas[1])
            plt.title(name)
            
            # Guarda el gráfico como un archivo .png en la carpeta Graficos.
            plt.savefig(f'Graficos/{name}.png')
            
            # Limpia la figura para que no se acumulen los gráficos en cada iteración.
            plt.clf()

    def grafico_area(self, names):
        """
        Crea gráficos de área a partir de los datos en archivos CSV.

        Args:
        - names: una lista de strings con los nombres de los archivos CSV.

        Returns:
        - None

        Raises:
        - FileNotFoundError: Si alguno de los archivos CSV no existe.
        """
        for i in range(len(names)):
            try:
                df_g=pd.read_csv(f'Resultados/p{names[i]}.csv',sep=",")
            except FileNotFoundError:
                print(f"Error: el archivo p{names[i]}.csv no se pudo encontrar.")
                continue
            columnas = df_g.columns
            # Define la paleta de colores de Seaborn a utilizar.
            colors = sns.color_palette('pastel')[0:5]
            # Crea el gráfico de área.
            plt.fill_between(df_g[columnas[0]][0:5], df_g[columnas[1]][0:5], color=colors[0], alpha=0.5)
            plt.plot(df_g[columnas[0]][0:5], df_g[columnas[1]][0:5], color=colors[0])
            plt.xlabel(columnas[0])
            plt.ylabel(columnas[1])
            plt.title(names[i])
            plt.savefig(f'Graficos/{names[i]}.png')
            plt.clf()

    def grafico_barras_hor(self, names):
        """
        Crea gráficos de barras horizontales para los archivos .csv con los nombres especificados en la lista names.

        Args:
        - names: lista de strings con los nombres de los archivos .csv a utilizar.

        Returns:
        - None.

        Raises:
        - FileNotFoundError: Si alguno de los archivos CSV no existe.
        """
        for i in range(len(names)):
            try:
                df_g=pd.read_csv(f'Resultados/p{names[i]}.csv',sep=",")
            except FileNotFoundError:
                raise FileNotFoundError(f'No se encontró el archivo p{names[i]}.csv')
            columnas = df_g.columns
            # Define la paleta de colores de Seaborn a utilizar.
            colors = sns.color_palette('pastel')[0:5]
            # Crea el gráfico de barras horizontales.
            plt.barh(df_g[columnas[0]][0:5], df_g[columnas[1]][0:5], color=colors)
            plt.xlabel(columnas[1])
            plt.ylabel(columnas[0])
            plt.title(names[i])
            plt.savefig(f'Graficos/{names[i]}.png')
            plt.clf()

    def grafico_caja(self, names):
        """
        Crea gráficos de caja y bigotes para los archivos .csv con los nombres especificados en la lista names.

        Args:
        - names: lista de strings con los nombres de los archivos .csv a utilizar.

        Returns:
        - None.
        
        Raises:
        - FileNotFoundError: Si alguno de los archivos CSV no existe.
        """
        for i in range(len(names)):
            try:
                df_g=pd.read_csv(f'Resultados/p{names[i]}.csv',sep=",")
            except FileNotFoundError:
                raise FileNotFoundError(f"No se encontró el archivo 'p{names[i]}.csv' en la carpeta 'Resultados'.")
            columnas = df_g.columns
            # Define la paleta de colores de Seaborn a utilizar.
            colors = sns.color_palette('pastel')[0:5]
            # Crea el gráfico de caja y bigotes.
            plt.boxplot(df_g[columnas[1]][0:5], labels=df_g[columnas[0]][0:5], patch_artist=True, boxprops=dict(facecolor=colors[0], color=colors[0]))
            plt.xlabel(columnas[0])
            plt.ylabel(columnas[1])
            plt.title(names[i])
            plt.savefig(f'Graficos/{names[i]}.png')
            plt.clf()
