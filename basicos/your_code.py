import pandas as pd 

# Cargar el marco de datos
df = pd.read_csv('C:/Users/Windows/Desktop/Repositorios/pandas/GoogleApps.csv')


# ¿Cuál es el nombre de la primera aplicación en el conjunto de datos?
print(df.head()) #Muestra los primeros 5 registros

# ¿A qué categoría pertenece la última aplicación del conjunto de datos?
print(df.tail()) #Muestra los ultimos 5 registros

# ¿Cuántas columnas hay en el conjunto de datos?
print(df.describe()) #Resumen del dataframe, muestra solo columnas con int o float, si queres todas -> 
print(df.shape[0]) #Cantidad de filas
print(df.shape[1]) #Cantidad de columnas
print(df.columns) #Lista de columnas
# ¿Qué tipo de datos se almacenan en cada una de las columnas?
print(df.dtypes)


# Especifique la media aritmética y la mediana del tamaño de la aplicación (Tamaño)
print("Media:", df["Size"].mean())
print("Mediana:", df["Size"].quantile(0.5))
# ¿Cuánto cuesta la aplicación más cara?

print("App mas cara", df[df["Type"] == "Paid"]["Price"].min())
# * Especifique la media aritmética y la mediana del número de instalaciones de aplicaciones (Instalaciones)