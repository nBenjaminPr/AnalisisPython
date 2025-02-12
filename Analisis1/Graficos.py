import matplotlib.pyplot as plt
import seaborn as sns

def grafico_ventas_ubicacion(df_ventas):
    """Genera un gráfico de barras con las ventas por ubicación."""
    df_ventas.plot(kind="bar", figsize=(10, 5), color="skyblue")
    plt.title("Ventas Totales por Ubicación")
    plt.xlabel("Ubicación Clave")
    plt.ylabel("Total de Ventas")
    plt.xticks(rotation=45)
    plt.show()

def histograma_costos(df):
    """Genera un histograma de la distribución de costos."""
    plt.hist(df["Costo"], bins=20, color="orange", edgecolor="black")
    plt.title("Distribución de Costos")
    plt.xlabel("Costo")
    plt.ylabel("Frecuencia")
    plt.show()


