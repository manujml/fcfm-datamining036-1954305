import pandas as pd
import matplotlib.pyplot as plt

sismos_especificos = pd.DataFrame({
    'Fecha': ['2023-08-31', '2023-08-31', '2023-08-31', '2023-08-31', '2023-08-31'],
    'Magnitud': [4.2, 3.2, 3.7, 4.1, 3.5],
    'Latitud': [16.81, 15.94, 18.07, 14.29, 15.86],
    'Longitud': [-94.87, -97.07, -103.25, -93.06, -97.32],
    'Localizacion': ['MATIAS ROMERO, OAX', 'PUERTO ESCONDIDO, OAX', 'COALCOMAN, MICH',
                     'CD HIDALGO, CHIS', 'RIO GRANDE, OAX']
})

plt.figure(figsize=(8, 6))
plt.scatter(sismos_especificos['Longitud'], sismos_especificos['Latitud'], s=sismos_especificos['Magnitud']*10,
            c=sismos_especificos['Magnitud'], cmap='viridis', alpha=0.7, edgecolors='w')

# Etiquetas y título del gráfico
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Primeros cinco sismos específicos')

# Mostrar la barra de color para representar la magnitud
plt.colorbar(label='Magnitud')

# Mostrar la imagen
plt.show()