import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# archivo CSV local
df = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/csv/SISMOS_MEX_v2.csv')

# convertir columna 'Fecha' a datetime por si las dudas xd
df['Fecha'] = pd.to_datetime(df['Fecha'])

# ordenar Sismos por magnitud (de mayor a menor)
df = df.sort_values(by='Magnitud', ascending=False)

# los cinco sismos más fuertes (para el forecasting)
top_5_sismos = df.head(5)

# Puntos críticos (sismos con magnitud +8.0)
umb = 8.0 # ajustar puntos (magnitud)
puntos_criticos = df[df['Magnitud'] >= umb]

# Aquí se entrena el modelo de regresión lineal para predecir la ubicación de los sismos basados en su magnitud y localización
md = LinearRegression()
X = df[['Magnitud', 'Longitud', 'Latitud']]  # Sismos pasados
y = df['Fecha']  # Fechas sismos pasados
md.fit(X, y)

# Forecasting de la ubicación de los siguientes cinco sismos
nuevos_sismos = df.tail(5)[['Magnitud', 'Longitud', 'Latitud']]
predicciones = md.predict(nuevos_sismos)

# grafica de todos los sismos (incluyendo puntos críticos y los siguientes cinco)
plt.figure(figsize=(10, 6))

# sismos
plt.scatter(df['Longitud'], df['Latitud'], color='blue', label='Sismos')

# cinco sismos más fuertes
plt.scatter(top_5_sismos['Longitud'], top_5_sismos['Latitud'], color='red', label='Top 5 Sismos')

# puntos críticos
plt.scatter(puntos_criticos['Longitud'], puntos_criticos['Latitud'], color='orange', label='Puntos Críticos')

# próximos cinco sismos (forecasting)
plt.scatter(nuevos_sismos['Longitud'], nuevos_sismos['Latitud'], color='green', label='Próximos 5 Sismos')

plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Forecasting Sismos MEX 2023 (Agosto a Septiembre)')
plt.legend()
plt.grid(True)
plt.savefig('Forescating_Sismos2023.png')
plt.show()