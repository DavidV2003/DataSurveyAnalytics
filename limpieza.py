
import pandas as pd
import os



class limpieza:

    def crear_carpeta_graficos(self):
        if not os.path.exists("Graficos"):
            os.makedirs("Graficos")
            print("La carpeta 'Graficos' ha sido creada exitosamente")
        else:
            print("La carpeta 'Graficos' ya existe")

    def crear_carpeta_resultados(self):
        if not os.path.exists("Resultados"):
            os.makedirs("Resultados")
            print("La carpeta 'Resultados' ha sido creada exitosamente")
        else:
            print("La carpeta 'Resultados' ya existe")

    def combinar_index(self, df):
        """
        Combina las columnas del DataFrame 'df' que tienen nombres repetidos, añadiendo información sobre el índice.
        Devuelve un nuevo DataFrame con las columnas renombradas.

        Args:
        - df (pandas.DataFrame): DataFrame que contiene las columnas a combinar.

        Returns:
        - pandas.DataFrame: Nuevo DataFrame con las columnas renombradas.
        """
        x = list(df.columns)
        n = str()
        c = -1
        iden = -1
        for i in range(len(x)):
            c += 1
            if x[i] != f'Unnamed: {c}':
                iden += 1
                n = x[i]
                x[i] = str(x[i]) + '**' + str(df[x[i]][0]) + '__' + str(iden)
            else:
                x[i] = str(n) + '**' + str(df[x[i]][0]) + '__' + str(iden)
        df = df.drop([0])
        array = df.to_numpy()
        df_new = pd.DataFrame(array, columns=x)
        return df_new

    def isNaN(self, string):
        """
        Verifica si un valor es NaN (Not a Number).

        Parámetros:
        string -- El valor que se desea verificar.

        Retorna:
        True si es NaN, False de lo contrario.
        """
        return string != string

    def preguntas(self, df_o, output_path):
        """
        Crea un diccionario con las preguntas correspondientes a cada columna del DataFrame df_o.

        Args:
            df_o (pandas.DataFrame): DataFrame de entrada que contiene los datos.
            output_path (str): Ruta del archivo Excel de salida.

        Returns:
            dict: Un diccionario donde las llaves son P1, P2, ..., Pn (siendo n la cantidad de columnas no nulas de df_o) y 
            los valores son las preguntas correspondientes a cada columna.

        Raises:
            ValueError: Si el argumento `df_o` no es un objeto pandas DataFrame o si la ruta del archivo de salida no 
            termina en ".xlsx".

        Exporta:
            Un archivo Excel llamado "preguntas.xlsx" con los resultados de la función.
        """
        if not isinstance(df_o, pd.DataFrame):
            raise ValueError("El argumento `df_o` debe ser un objeto pandas DataFrame.")

        if not output_path.endswith(".xlsx"):
            raise ValueError("La ruta del archivo de salida debe terminar en '.xlsx'.")
        c=0
        preguntas = {}
        limpias=[]
        for i in range(len(df_o.columns)):
            if df_o.columns[i] != f'Unnamed: {i}':
                limpias.append(df_o.columns[i])
                c+=1

        for j in range(len(limpias)):
            preguntas[f'P{j+1}'] = limpias[j]
        
        # Convierte el diccionario en un DataFrame de pandas
        preguntas_df = pd.DataFrame.from_dict(preguntas, orient='index', columns=['Pregunta'])

        # Exporta el DataFrame a un archivo Excel
        preguntas_df.to_excel(output_path, index_label='Pregunta')

        return preguntas
    

    def count(self,df):
        """
        Cuenta la cantidad de ocurrencias de cada valor en cada columna del DataFrame df y genera un archivo CSV y una
        gráfica de pastel para cada una de ellas.

        Parámetros:
        df -- El DataFrame para el cual se desea realizar el conteo.

        Retorna:
        Un mensaje de confirmación de que las gráficas fueron creadas.
        """
        dic={}
        main=[]
        for i in range(df.shape[1]):
            aux=[]
            for j in range(df.shape[1]):
                txt=df.columns[j]
                divisiones=txt.split("__")
                divisiones[1]
                if divisiones[1]==str(i):
                    aux.append(df.columns[j])
            try:
                aux[0]
                main.append(aux)
            except:
                pass

        for t in range(len(main)):
            d={}
            for y in main[t]:
                d[y]=df[y]
            dft=pd.DataFrame(data=d)
            filaarr=[]
            #Crear 1 sola columna con arrays

            #Drop NAN
            for i in range(dft.shape[0]):
                x=[]
                for j in range(dft.shape[1]):
                    if self.isNaN(dft[dft.columns[j]][i])!=True:
                        x.append(dft[dft.columns[j]][i])
                filaarr.append(x)

            #Opciones posibles sin duplicados
            total=[]
            for i in range(len(filaarr)):
                for j in range(len(filaarr[i])):
                    if filaarr[i][j] not in total:
                        total.append(filaarr[i][j])

            #Releer todo y mirar cuantas veces esta
            c2=[]
            for h in total:
                contador=0
                for i in range(len(filaarr)):
                    for j in range(len(filaarr[i])):
                        if filaarr[i][j] == h:
                            contador+=1
                c2.append(contador)

            txt=str(main[t])
            dic={}
            nombre=t+1
            dic[nombre]=total
            dic[f'Conteo']=c2
            dft=pd.DataFrame(data=dic)
            dft.to_csv(f'Resultados/{nombre}.csv', index=False)
        return 'Csv creadas'
