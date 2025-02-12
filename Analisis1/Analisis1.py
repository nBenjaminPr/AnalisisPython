import pandas as pd

df = pd.read_excel("C:/Users/Usuario/Desktop/Escriotrio Nico/PYTHON/PRACTICA_MIERCOLES/Analisis1/Ventas.xlsx")






df_grouped_ubicacion = df.groupby("Ubicación Clave")["Ventas"].sum()
print(df_grouped_ubicacion.head(5)) #Muestra la suma total de ventas por ubicación.

df_ganancia_producto = df.groupby("Clave Producto")["Utilidad"].sum()
print(df_ganancia_producto.head(5)) #Suma la utilidad total por cada producto.

df_vendedor = df.groupby("Clave Vendedor")[["Ventas", "Cantidad"]].sum()
print(df_vendedor.head(5))#Agrupa por vendedor y muestra el total de ventas y la cantidad de productos vendidos.

df_descuento = df.groupby("Ubicación Clave")["Descuento"].mean()
print(df_descuento.head(5))#Muestra el descuento promedio en cada ubicación.

print (df.head(5))  #Visualización de las primeras 5 filas

print(df.info()) #Info sobre el dataset
print(df.describe()) #Estadisticas generales
df.dropna(inplace=True)  # Eliminar filas con valores nulos
df.fillna(0, inplace=True)  # Reemplazar nulos con 0