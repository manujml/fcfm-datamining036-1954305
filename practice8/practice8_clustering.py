import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# carga csv localmente (nueva version)
data = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/csv/SISMOS_MEX_v2.csv')

# convertir columna 'Fecha' a datetime por si las dudas xd
data['Fecha'] = pd.to_datetime(data['Fecha'])

# datos desde el 1ro de Enero de 2023 hasta el 30 de Agosto de 2023
start_date = pd.to_datetime('2023-01-01')
end_date = pd.to_datetime('2023-08-30')
filtered_data = data[(data['Fecha'] >= start_date) & (data['Fecha'] <= end_date)]

# columna 'Magnitud'
magnitudes = filtered_data['Magnitud'].values.reshape(-1, 1)

# KMeans k=3
kmeans = KMeans(n_clusters=3)
kmeans.fit(magnitudes)
clusters = kmeans.predict(magnitudes)

# columna clusters
filtered_data['Cluster'] = clusters

# Grafica
plt.figure(figsize=(10, 6))

for cluster in filtered_data['Cluster'].unique():
    cluster_data = filtered_data[filtered_data['Cluster'] == cluster]
    plt.scatter(cluster_data['Fecha'], cluster_data['Magnitud'], label=f'Grupo{cluster+1}')

plt.title('Clustering Sismos (Ene 2023 - Ago 2023)')
plt.xlabel('Fecha')
plt.ylabel('Magnitudes')
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('clustering2023.png')
plt.show()