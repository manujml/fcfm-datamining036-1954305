import pandas as pd

df = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/SISMOS_MEX_1975-2023.csv')

# Borra todas las cadenas antes de la cadena 'de ', incluyendo a dicha cadena
df['Referencia de localizacion'] = df['Referencia de localizacion'].str.split('de ').str[1].str.strip()

# Cambiando el nombre de la columna 'Referencia de localizacion'
new_name = 'Localizacion'
df = df.rename(columns={'Referencia de localizacion': new_name})

# Elimina las filas que incluyan 'no calculable' en la columna 'Magnitud'
df = df[df['Magnitud'] != 'no calculable']

# Eliminando columnas 'Latitud' y 'Longitud'
delete_col = ['Latitud', 'Longitud']
df = df.drop(delete_col, axis=1)

# Guarda el nuevo csv con los datos limpios
df.to_csv('SISMOS_MEX_Practice2.csv', index=False)