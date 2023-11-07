import pandas as pd

# Leyendo el archivo csv
df = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/practice9/newdata/SSNMX_catalogo_20230831_20231101.csv')
                    # ↑ cambiar la dirección en donde se encuentra el archivo localmente en el dispositivo

# Borrar todas las cadenas antes de la cadena 'de ', incluyendo a dicha cadena
df['Referencia de localizacion'] = df['Referencia de localizacion'].str.split('de ').str[1].str.strip()

#convertir a fecha
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Cambiando el nombre de la columna 'Referencia de localizacion'
new_name = 'Localizacion'
df = df.rename(columns={'Referencia de localizacion': new_name})

# Había datos que tenían la cadena 'en revision', por lo que se tuvieron que omitir
# df = df[~df['Profundidad'].str.contains('en revision', na=False)]
# Convertir a datos numéricos por si las dudas xd
df['Profundidad'] = pd.to_numeric(df['Profundidad'], errors='coerce')

# Elimina las filas que incluyan 'no calculable' en la columna 'Magnitud', puesto que no se puede trabajar con dichos datos
dlte_rows = df[df['Magnitud'] == 'no calculable'].index
df.drop(dlte_rows, inplace=True)

#eliminar columnas
del(df['Hora'])
del(df['Fecha UTC'])
del(df['Hora UTC'])
del(df['Estatus'])

# Guarda el nuevo csv con los datos limpios
df.to_csv('SISMOS_1_NOV_2023.csv', index=False)