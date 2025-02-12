import pandas as pd

df = pd.read_excel("C:/Users/Usuario/Desktop/Escriotrio Nico/PYTHON/PRACTICA_MIERCOLES/Analisis1/Ventas.xlsx")

print (df.head(5)) #Visualización de las primeras 5 filas
print(df.info()) #Info sobre el dataset
print(df.describe()) #Estadisticas generales