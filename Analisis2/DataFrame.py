import pandas as pd

#Datos en formato de listas

categorias = ["ropa","juegos","deportes","hogar"]
ventas = [1200,80,950,1100,700 ]
descuentos= [10,2,15,5,30]

#Creando Df

df= pd.DataFrame (list(zip(categorias,ventas,descuentos)),columns=["Categoría", "Ventas", "Descuento"])

print (df)

#Crear un DataFrame desde un Diccionario

data = {
        "Producto": ["Laptop", "Camisa", "Sofá", "Bicicleta", "Muñeca"],
        "Precio": [1000, 50, 600, 400, 25],
        "Stock": [10, 200, 5, 15, 100]
}

df = pd.DataFrame(data)

print (df)