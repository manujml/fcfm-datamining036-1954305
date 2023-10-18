import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

# Se carga el csv localmente
data = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/csv/SISMOS_MEX_1975-2023.csv')

# Convertir los datos a numéricos (por si las dudad)
data['Magnitud'] = pd.to_numeric(data['Magnitud'], errors='coerce')

# Se establecen los límites de los rangos de magnitud y etiquetar
rangos_magnitud = [6.0, 7.0, 8.0, float('inf')]
tags = ['6.0-6.9', '7.0-7.9', '8.0+']

# rangos de todas las magnitudes
# rangos_magnitud = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, float('inf')]
# tags = ['1.0-1.9', '2.0-2.9', '3.0-3.9', '4.0-4.9', '5.0-5.9', '6.0-6.9', '7.0-7.9', '8.0+']

# Aquí se clasifican los sismos según su magnitud (de 6.0-6.9, 7.0 a 7.9 y 8.0+), así como asignar un color a cada rango
data['Clasificación'] = pd.cut(data['Magnitud'], bins=rangos_magnitud, labels=tags)
colors = sns.color_palette("viridis", n_colors=len(tags))

# Se crea una dispersión con puntos de diferentes colores
plt.figure(figsize=(14, 12))
sns.scatterplot(data=data, x='Longitud', y='Latitud', hue='Clasificación', palette=colors, s=50)

# Cargar el mapa de México usando gpd
mexico = gpd.read_file('mexicoHigh.json')
mexico.boundary.plot(ax=plt.gca(), linewidth=2, color='black')

# Configurar la imagen
plt.title('Clasificación | Sismos por Magnitud')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.grid(True)

# Límites de ejes X e Y para centrar el mapa en México (masomenos donde se localiza México de acuerdo a Latitud y Longitud)
plt.xlim(-120, -80)
plt.ylim(15, 35)

# Simbología de las magnitudes (colores, significado)
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label) for color, label in zip(colors, tags)]
plt.legend(handles=handles, title='Magnitud')

# Guardar la imagen
plt.savefig('clasificacion_magnitud.png')

# Mostrar la imagen en pantalla
plt.show()