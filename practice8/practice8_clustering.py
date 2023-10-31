import pandas as pd
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# Se carga el csv localmente
data = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/csv/SISMOS_MEX.csv')  # Asegúrate de colocar el nombre de tu archivo

# crear columna 'Grupo' en rangos de magnitudes
data['Grupo'] = pd.cut(data['Magnitud'],
                       bins=[6.0, 7.0, 8.0, float('inf')],
                       labels=['6.0-6.9', '7.0-7.9', '8.0+'])

# preproceso columna 'fecha' para convertirla a formato numérico
data['Fecha'] = pd.to_datetime(data['Fecha'], format='%d/%m/%Y')  # Convertir a tipo datetime

# cantidad de días transcurridos desde una fecha de referencia (1ro de enero de 1975)
fecha_referencia = pd.to_datetime('01/01/1970')  # Selecciona una fecha de referencia
data['dias_transcurridos'] = (data['Fecha'] - fecha_referencia).dt.days

# columnas relevantes para el clustering
data_clustering = data[['dias_transcurridos', 'Profundidad']]  # Seleccionar las columnas relevantes

# valores faltantes
data_clustering = data[['dias_transcurridos', 'Profundidad']]  # Seleccionar las columnas relevantes
imputer = SimpleImputer(strategy='mean')
data_clustering = imputer.fit_transform(data_clustering)

# modelo KMeans
k_optimo = 3
kmeans = KMeans(n_clusters=k_optimo, random_state=42)
clusters = kmeans.fit_predict(data_clustering)

# columna clusters
data['Grupo'] = clusters

# Visualización de los clusters
plt.figure(figsize=(24, 20))
colors = {0: 'red', 1: 'blue', 2: 'green'}

for cluster_id in range(k_optimo):
    cluster_data = data[data['Grupo'] == cluster_id]
    plt.scatter(cluster_data['dias_transcurridos'], cluster_data['Profundidad'], color=colors[cluster_id], label=f'Grupo{cluster_id+1}')

print(clusters)
plt.title(f'Clustering con KMeans')
plt.xlabel('Días Transcurridos desde el 01/Enero/1975')
plt.ylabel('Profundidad')
plt.legend()
plt.savefig('clustering.png')
plt.show()