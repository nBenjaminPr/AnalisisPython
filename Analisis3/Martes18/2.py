import pandas as pd
import numpy as np

#Datos en forma de lista 

Ropa = ["Camisetas","Pantalones","Zapatillas", "Gorra"]
Precio = [2000, 4000, 5000, 1000]

#Creo el DF

df = pd.DataFrame (list(zip(Ropa,Precio)), columns= ["Ropa","Precio"])

#print (df)


#Merge y Join

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Nombre': ['Ana', 'Luis', 'Carlos']})

df2 = pd.DataFrame({'ID': [1, 2, 4], 'Salario': [1000, 1500, 2000]})
df_merge = df1.merge(df2, on="ID", how= "left") #Solo id comunes

print (df1)
print (df2)

print(df_merge)

#🚀 Explicación rápida de los JOINs en Pandas:

#LEFT JOIN: Mantiene todas las filas del primer DataFrame y solo las coincidentes del segundo.
#RIGHT JOIN: Mantiene todas las filas del segundo DataFrame y solo las coincidentes del primero.
#OUTER JOIN: Mantiene todas las filas de ambos DataFrames.