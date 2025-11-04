import pandas as pd
df = pd.read_csv('C:/Users/Windows/Desktop/Repositorios/pandas/GoogleApps.csv')

# ¿Cuál es el precio de la aplicación de pago más barata (tipo == 'Pagada')?
print("Precio de la app de pago mas barata:", df[df['Type']=='Paid']['Price'].min())

# ¿Cuál es el número medio de instalaciones para las aplicaciones de la categoría "ART_AND_DESIGN"?
print("Mediana de instalaciones para categoria ART_AND_DESIGN:", df[df['Category']=='ART_AND_DESIGN']['Installs'].quantile(0.5))

# ¿Cuánto más es el número máximo de Reseñas para aplicaciones gratuitas (tipo == 'Gratis')
# que el número máximo de Reseñas para aplicaciones pagas (Tipo == 'Pagado')?
resenas_pagas = df[df['Type']=="Paid"]['Reviews'].max()
resenas_gratis = df[df['Type']!="Paid"]['Reviews'].max()
print("Diferencia entre el número maximo de reseñas de pago y gratuitas:", resenas_gratis - resenas_pagas)

# ¿Cuál es el tamaño mínimo de una aplicación para adolescentes (Clasificación de contenido == 'Adolescente')?
print("Tamaño mínimo de una aplicación para adolescentes:", df[df['Content Rating']=='Teen']['Size'].min())

# * ¿Cuál es la categoría de una aplicación que tiene la mayor cantidad de reseñas?
resena_max = df['Reviews'].max()
app_max_resena = df[df['Reviews']==resena_max]
print("Categoría con mas reseñas:", app_max_resena['Category'].values[0])

# * ¿Cuál es la calificación media de las aplicaciones cuyo precio supera los $ 20 y
# ¿El número de instalaciones es superior a 10,000?
media_app = df[(df['Price']>20) & (df['Installs']>10000)]['Rating'].mean()
print("clasificación media de app con precio mayor a 20 e instalaciones mayores a 10mil:", media_app)