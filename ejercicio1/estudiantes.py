import kagglehub
import pandas as pd
import os

# 1. Descargar dataset 
path = kagglehub.dataset_download("spscientist/students-performance-in-exams")

print("Archivos descargados en:", path)
print("Contenido:", os.listdir(path))

# 2. Cargar el CSV 
df = pd.read_csv(os.path.join(path, "StudentsPerformance.csv"))

print(df.info())

print("PUNTAJE DE HABILIDADES")
print(df.describe())

print("PUNTAJE DE HABILIDADES DE CHICOS QUE HICIERON EL CURSO  DE PREPARACION")
print(df[df['test preparation course']=='completed'].describe())

print("PUNTAJE DE HABILIDADES DE CHICOS QUE NO HICIERON EL CURSO  DE PREPARACION")
print(df[df['test preparation course']=='none'].describe())

print("PUNTAJES PROMEDIOS POR NIVEL ACADEMICO DE LOS PADRES")
print(df.groupby(by='parental level of education')[['math score',  'reading score',  'writing score']].agg(['mean', 'min', 'max']))
print(df.groupby(by='test preparation course')[['math score',  'reading score',  'writing score']].agg(['mean', 'min', 'max']))


print(df.pivot_table(index='parental level of education',
                    columns='test preparation course',
                    values=['math score'],
                    aggfunc= ['mean', 'min', 'max'] 
                    ))

print("PUNTAJE POR GENEROS:")
print(df.groupby(by='gender')[['math score',  'reading score',  'writing score']].agg(['mean', 'min', 'max', 'median']))

print("PUNTAJE POR COMIDA:")
print(df.groupby(by='lunch')[['math score',  'reading score',  'writing score']].agg(['mean', 'min', 'max', 'median']))

print(df.pivot_table(index='lunch',
                    columns='test preparation course',
                    values=['math score'],
                    aggfunc= ['mean', 'min', 'max'] 
                    ))
df_math = df[
    (df['reading score'] > 69) &
    (df['writing score'] > 69) &
    (df['math score'] > 69)
]

total_mejores_genero = df_math['gender'].value_counts()
total_mejores_parental = df_math['parental level of education'].value_counts()
total_mejores_lunch = df_math['lunch'].value_counts()

print(total_mejores_genero)
print(total_mejores_parental)
print(total_mejores_lunch)