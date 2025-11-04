import pandas as pd
df = pd.read_csv('C:/Users/Windows/Desktop/Repositorios/pandas/GoogleApps.csv')

# 1 ¿Cuántas aplicaciones hay en la 'Category' 'BUSINESS' 'Category'?
temp = df['Category'].value_counts()
temp = temp['BUSINESS']
print("Aplicaciones totales en categoria BUSINESS:", temp )

# 2 ¿Cuál es la relación de aplicaciones para adolescentes ('Teen') y 
# las destinadas para niños mayores de 10 años ('Everyone 10+')?
# Redondee la respuesta a la centésima más cercana.
apps_content = df['Content Rating'].value_counts()
apps_teen = apps_content['Teen']
apps_10 = apps_content['Everyone 10+']
print("Relacion de cantidad de apps teen / apps +10:", round(apps_teen / apps_10, 3))

# 3.1 ¿Cuál es el 'Rating' promedio de aplicaciones 'Paid'? 
# Redondee la respuesta a la centésima más cercana.
apps_paid = df.groupby(by='Type')['Rating'].mean()
apps_rating_paid = apps_paid['Paid']
print("Rating promedio de aplicaciones pagas:", round(apps_rating_paid, 2))

# 3.2 ¿Cuánto más bajo es el 'Rating' promedio de aplicaciones 'Free' que el 
# promedio de valoración de las aplicaciones 'Paid'?
# Redondee la respuesta a la centésima más cercana.
apps_promedio_rating = df.groupby(by = 'Type')['Rating'].mean()
apps_free_promedio_rating = apps_promedio_rating['Free']
apps_paid_promedio_rating = apps_promedio_rating['Paid']
diferencia = apps_paid_promedio_rating - apps_free_promedio_rating
print("El promedio de rating de las apps pagas tienen una diferencia con el promedio de la gratuitas en:", round(diferencia, 2))


# 4 ¿Cuál es el 'Size' (tamaño) mínimo y máximo en la 'Category' 'COMICS'?
# Redondee la respuesta a la centésima más cercana.

# Bonificación 1. ¿Cuántas aplicaciones tienen un 'Rating' estrictamente superior a 4.5 en la 'Category' 'FINANCE'?

# Bonificación 2. ¿Cuál es la relación de juegos 'Free' y 'Paid' con un 'Rating' superior a 4.9?


