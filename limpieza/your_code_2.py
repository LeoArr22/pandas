import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv('GoogleApps.csv')

# print(df.describe())
# ¿Cuál es el precio de la aplicación de pago más barata (tipo == 'Pagada')?
# apps_pagas = df[(df['Type']!='Free')]
# print(apps_pagas.sort_values('Price').head())
# ¿Cuál es el número medio de instalaciones?
# para las aplicaciones de la categoría "ART_AND_DESIGN"?


# ¿Cuánto más es el número máximo de Reseñas para aplicaciones gratuitas (tipo == 'Gratis')
# que el número máximo de Reseñas para aplicaciones pagas (Tipo == 'Pagado')?


# ¿Cuál es el tamaño mínimo de una aplicación para adolescentes (Clasificación de contenido == 'Adolescente')?


# * ¿Cuál es la categoría de una aplicación que tiene la mayor cantidad de reseñas?


# * ¿Cuál es la calificación media de las aplicaciones cuyo precio supera los $ 20 y
# ¿El número de instalaciones es superior a 10,000?