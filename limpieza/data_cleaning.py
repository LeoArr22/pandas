import pandas as pd

def reemplaza_cadena(size):
    if size == 'Varies with device':
        return -1
    return size

def borra_letra(size):
    if size != -1:
        op = 1
        if size[-1] == 'k':
            op = 1024
        size = float(size[:-1]) / op
    return size
    


df = pd.read_csv('C:/Users/Alumno/Documents/pandas/GooglePlayStore_wild.csv')
# Imprimir información sobre todo el DataFrame para ver qué columnas hay que limpiar
print(df.info())
# Imprimir información sobre todo el DataFrame para ver qué columnas hay que limpiar
print('Valores con datos y null:\n', pd.isnull(df['Rating']).value_counts())

# ¿Cuántas aplicaciones en el conjunto de datos no tienen ('NaN') clasificación ('Rating')?


# Reemplazar el valor nulo ('NaN') de la clasificación ('Rating') para tales aplicaciones con -1.
df['Rating'].fillna(-1, inplace = True)
print(df.info())

# Determinar qué otro valor de tamaño ('Size') se almacena en el conjunto de datos además de Kilobytes y Megabytes, y reemplazar por -1.
# Convertir los tamaños ('Size') de aplicación a formato numérico (float). Los tamaños de todas las aplicaciones deben medirse en Megabytes.
print(df['Size'])

print("CANTIDAD DE 'Varies with device':", (df['Size'] == 'Varies with device').sum())
print('Varía con el dispositivo - 1695')
df['Size']=df['Size'].apply(reemplaza_cadena)
df['Size']=df['Size'].apply(borra_letra)

print(df['Size'])

# ¿Cuál es el tamaño máximo 'Size' de las aplicaciones en 'Category' 'TOOLS'?
tam_size_max = df[df['Category']=='TOOLS']['Size'].max()
print('Tamaño maximo:', tam_size_max)


# Tareas adicionales
# Reemplazar el tipo de datos por entero (int) para el número de instalaciones ('Installs').
# En la entrada del número de instalaciones ('Installs'), el signo "+" debe ser ignorado.
# Esto significa que si el número de instalaciones en el conjunto de datos es 1,000,000+, necesita cambiar el valor a 1000000

# Agrupar los datos por 'Category' y público objetivo ('Content Rating') como prefiera
# calcular el número promedio de instalaciones ('Installs') para cada grupo Redondear la respuesta a la centésima más cercana.
# En la tabla resultante, encontrar la celda con el mayor valor. 
# ¿A qué grupo de edad y tipo de aplicación pertenecen los datos de esa celda?

# ¿Qué aplicación no tiene un 'Type' especificado? ¿Qué tipo debe introducirse allí en función del precio?

# Imprimir información sobre todos los DataFrames para asegurarse de que la limpieza se ha realizado con éxito
