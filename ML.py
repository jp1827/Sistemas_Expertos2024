import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Datos de ejemplo: tamaño de la casa en metros cuadrados y su precio
# Puedes modificar estos datos para ver cómo cambia el modelo
tamanos = np.array([50, 60, 70, 80, 90, 100, 120, 220]).reshape(-1, 1)  # Tamaños en m²
precios = np.array([150000, 180000, 210000, 240000, 270000, 300000, 360000, 400000])  # Precios en $

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(tamanos, precios, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(X_train, y_train)

# Realizar predicciones
predicciones = modelo.predict(X_test)

# Mostrar resultados
for tamaño, precio_real, precio_predicho in zip(X_test, y_test, predicciones):
    print(f"Tamaño: {tamaño[0]} m² | Precio real: ${precio_real} | Precio predicho: ${precio_predicho:.2f}")

# Graficar los resultados
plt.scatter(tamanos, precios, color='blue', label='Datos reales')
plt.plot(tamanos, modelo.predict(tamanos), color='red', label='Modelo de regresión')
plt.title('Regresión Lineal: Precio de Casas')
plt.xlabel('Tamaño (m²)')
plt.ylabel('Precio ($)')
plt.legend()
plt.grid()
plt.show()

