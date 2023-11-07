import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/csv/SISMOS_MEX_v2.csv')

# convertir columna 'Fecha' a tipo datetime por si las dudas xd
df['Fecha'] = pd.to_datetime(df['Fecha'])

# solo datos del 2023
df_2023 = df[df['Fecha'].dt.year == 2023]

# X fechas del año 2023
X = df_2023['Fecha'].dt.month.values.reshape(-1, 1)

# Y magnitudes
Y = df_2023['Magnitud']

# modelo de regresión lineal
regression = LinearRegression()
regression.fit(X, Y)

# coef regresión
m = regression.coef_[0]
b = regression.intercept_

# Crear la línea de regresión
regression_line = m * X + b

# Graficar los resultados
plt.figure(figsize=(14, 10))
plt.scatter(df_2023['Fecha'], Y, label='Magnitudes 2023')
plt.plot(df_2023['Fecha'], regression_line, color='red', label='Regresión Lineal')
plt.title('Regresión Lineal sobre las Magnitudes de Sismos 2023')
plt.xlabel('Fechas')
plt.ylabel('Magnitud')
plt.legend()
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('regresionlineal_2023.png')
plt.show()