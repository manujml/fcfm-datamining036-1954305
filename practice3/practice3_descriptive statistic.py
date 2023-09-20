import pandas as pd
import os

df = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/practice2/SISMOS_MEX.csv')

# Agrupar las localizaciones
gp_localizacion = df.groupby('Localizacion')

# V Obtener suma, conteo, media, moda, mediana, maximo y minimo de cada localizacion

# Suma de las magnitudes
suma_local = gp_localizacion['Magnitud'].sum()

# Obtención de media
media_local = gp_localizacion['Magnitud'].mean()
# Aquí la media se redondea a dos decimales
media_local = media_local.round(2)

# Obtención de la mediana
mediana_local = gp_localizacion['Magnitud'].median()
# Aquí la mediana se redondea a dos decimales
mediana_local = mediana_local.round(2)

# Obtención de la moda
moda_local = gp_localizacion['Magnitud'].agg(lambda x: x.mode().iloc[0])

# Obtención del máximo
max_local = gp_localizacion['Magnitud'].max()

# Obtención del mínimo
min_local = gp_localizacion['Magnitud'].min()

# Crear un nuevo DataFrame con las localizaciones agrupadas
SISMOS_ESTADISTICA = pd.DataFrame({
    'Suma': suma_local,
    'Media': media_local,
    'Mediana': mediana_local,
    'Moda': moda_local,
    'Max': max_local,
    'Min': min_local
})

SISMOS_ESTADISTICA.to_csv("SISMOS_ESTADISTICA.csv", index=False)