import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# carga csv localmente (nueva version)
df = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/csv/SISMOS_MEX_v2.csv')

# convertir columna 'Fecha' a datetime por si las dudas xd
df['Fecha'] = pd.to_datetime(df['Fecha'])

# datos desde el 1ro de Enero de 2023 hasta el 30 de Agosto de 2023
start_date = pd.to_datetime('2023-01-01')
end_date = pd.to_datetime('2023-08-30')
filtered_df = df[(df['Fecha'] >= start_date) & (df['Fecha'] <= end_date)]

# columna 'Magnitud'
magnitudes = filtered_df['Magnitud'].values.reshape(-1, 1)

# KMeans k=3
kmeans = KMeans(n_clusters=3)
kmeans.fit(magnitudes)
clusters = kmeans.predict(magnitudes)

# columna clusters
filtered_df['Cluster'] = clusters

# Grafica
plt.figure(figsize=(10, 6))

for cluster in filtered_df['Cluster'].unique():
    cluster_df = filtered_df[filtered_df['Cluster'] == cluster]
    plt.scatter(cluster_df['Fecha'], cluster_df['Magnitud'], label=f'Grupo{cluster+1}')

plt.title('Clustering Sismos (Ene 2023 - Ago 2023)')
plt.xlabel('Fecha')
plt.ylabel('Magnitudes')
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('clustering2023.png')
plt.show()