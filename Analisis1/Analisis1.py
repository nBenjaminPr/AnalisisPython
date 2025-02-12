import pandas as pd

def cargar_datos(ruta):
    """Carga los datos desde un archivo CSV y los devuelve como DataFrame."""
    df = pd.read_csv(ruta)
    return df

def ventas_por_ubicacion(df):
    """Agrupa las ventas por ubicación clave y devuelve el resultado."""
    return df.groupby("Ubicación Clave")["Ventas"].sum()

def ganancia_por_producto(df):
    """Agrupa la utilidad por clave de producto."""
    return df.groupby("Clave Producto")["Utilidad"].sum()

def resumen_vendedor(df):
    """Devuelve el total de ventas y cantidad por vendedor."""
    return df.groupby("Clave Vendedor")[["Ventas", "Cantidad"]].sum()

def descuento(df):
    """Muestra el descuento promedio en cada ubicación"""
    return df.groupby("Ubicación Clave")["Descuento"].mean()
