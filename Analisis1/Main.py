import pandas as pd
import Analisis1
import Graficos

#Carga datos

df = pd.read_excel("C:/Users/Usuario/Desktop/Escriotrio Nico/PYTHON/PRACTICA_MIERCOLES/Analisis1/Ventas.xlsx")

# Obtener análisis
ventas_ubicacion = Analisis1.ventas_por_ubicacion(df)

# Generar visualizaciones
Graficos.grafico_ventas_ubicacion(ventas_ubicacion)
Graficos.histograma_costos(df)