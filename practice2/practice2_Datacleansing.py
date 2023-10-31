import pandas as pd
import os

# Leyendo el archivo csv
df = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/csv/SISMOS_MEX_1975-2023.csv')
                    # ↑ cambiar la dirección en donde se encuentra el archivo localmente en el dispositivo

# Borrar todas las cadenas antes de la cadena 'de ', incluyendo a dicha cadena
df['Referencia de localizacion'] = df['Referencia de localizacion'].str.split('de ').str[1].str.strip()

# Cambiando el nombre de la columna 'Referencia de localizacion'
new_name = 'Localizacion'
df = df.rename(columns={'Referencia de localizacion': new_name})

# Había datos que tenían la cadena 'en revision', por lo que se tuvieron que omitir | recordar limpiar y actualizar csv
df = df[~df['Profundidad'].str.contains('en revision', na=False)]
# Convertir a datos numéricos por si las dudas xd
df['Profundidad'] = pd.to_numeric(df['Profundidad'], errors='coerce')

# Elimina las filas que incluyan 'no calculable' en la columna 'Magnitud', puesto que no se puede trabajar con dichos datos
dlte_rows = df[df['Magnitud'] == 'no calculable'].index
df.drop(dlte_rows, inplace=True)

# Guarda el nuevo csv con los datos limpios
df.to_csv('SISMOS_MEX.csv', index=False)