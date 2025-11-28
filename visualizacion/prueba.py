import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('C:/Users/Alumno/Documents/pandas/GoogleApps.csv')

print(df['Installs'].unique())