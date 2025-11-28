import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('C:/Users/Alumno/Documents/pandas/GoogleApps.csv')

# print(df['Size'].head())
# print(df['Install'].unique()[:20])
print(df.info())
print(df['Size'].describe())
#HISTOGRAMA -> Distribucion de valores entre min y max, frecuencia por intervalos
df['Size'].plot(kind = 'hist', bins = 10)
# plt.xticks(range(0, 101, 10))
plt.show()

#CAJA CON BIGOTE -> Detecta valores atipicos
# Mediana (línea en el medio de la caja)
# Q1 y Q3 (primer y tercer cuartil → definen la caja)
# IQR (rango intercuartílico = Q3 − Q1)
# Bigotes: se extienden hasta
# Q1 − 1.5 × IQR
# Q3 + 1.5 × IQR
# Puntos fuera de los bigotes → valores atípicos
# La gran cantidad de valores se concentran dentro de la caja, 
# pueden existir valores normales hasta los bigotes, y luego fuera son outliers
# print(df[df['Type'] == 'Paid']['Price'].head())
# print(df[df['Type'] == 'Paid']['Price'].unique()[:20])
print(df[df['Type'] == 'Paid']['Price'].describe())
df[df['Type'] == 'Paid']['Price'].plot(kind = 'box')
plt.ylim(0, 20)
plt.show()

#DISPERSION -> Analizar relaciones entre dos variables y detectar patrones, tendencias, correlaciones y outliers

#Relacion Nula
df.plot(kind='scatter', x='Price', y='Rating')
plt.xlim(0, 200)
plt.xticks(range(0, 201, 20))

print("Correlacion precio rating\n", df[['Price','Rating']].corr())
plt.show()


#Relacion debil
df.plot(kind='scatter', x='Reviews', y='Rating')
plt.xscale('log')
print("Correlacion reviews rating\n", df[['Reviews','Rating']].corr())
plt.show()



#Relacion nula
df.plot(kind='scatter', x='Price', y='Size')
plt.xlim(0, 200)
plt.xticks(range(0, 201, 20))
plt.yscale('log')
print("Correlacion precio tamaño\n", df[['Price','Size']].corr())
plt.show()

#Relacion fuerte
df.plot(kind='scatter', x='Installs', y='Reviews')
plt.xscale('log')
plt.yscale('log')
print("Correlacion Installs Reviews\n", df[['Reviews','Installs']].corr())
plt.show()


#GRAFICO DE TORTA - PIE
# Un gráfico de torta sirve para mostrar:
# Qué porcentaje representa cada categoría.
# Cómo se distribuye un total entre partes.
# No tantos elementos
df['Content Rating'].value_counts().plot(kind = 'pie')
plt.show()

#GRAFICO DE BARRAS
# Puedes ver fácilmente cuánto tiene cada categoría. Numero absoluto.
# Permite comparar magnitudes entre categorías de manera precisa.
# Permite mas cantidad de elementos
df['Category'].value_counts().plot(kind = 'bar')
plt.show()

df['Category'].value_counts().plot(kind = 'barh')
plt.show()

df['Category'].value_counts().plot(kind = 'barh', figsize = (20, 14), grid = True)
plt.show()

d1 = df[df['Type'] == 'Free'].groupby('Content Rating')['Installs'].mean()
d2 = df[df['Type'] == 'Paid'].groupby('Content Rating')['Installs'].mean()
d1.plot(kind = 'barh')
plt.show()

d2.plot(kind = 'barh')
plt.show()


d = df.pivot_table(index = 'Content Rating', 
 	columns = 'Type', 
 	values = 'Installs', 
 	aggfunc = 'mean'
  )
d.plot(kind='barh', subplots=True, sharey=True)
plt.xscale('log')
plt.show()

d.plot(kind='barh', subplots=True, sharey=True, layout=(1,2))
plt.xscale('log')
plt.show()


