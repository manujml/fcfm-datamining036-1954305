import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/practice2/SISMOS_MEX.csv')

# Había datos que tenían la cadena 'en revision', por lo que se tuvieron que omitir | recordar limpiar y actualizar csv
df = df[~df['Profundidad'].str.contains('en revision', na=False)]
# Convertir a datos numéricos por si las dudas xd
df['Profundidad'] = pd.to_numeric(df['Profundidad'], errors='coerce')

plt.figure(figsize=(24, 20))

# dispersión
plt.scatter(df['Magnitud'], df['Profundidad'], alpha=0.5)

plt.xlabel('Magnitud')
plt.ylabel('Profundidad')

plt.title('Dispersión de Magnitud | Profundidad')

plt.savefig('correlation.png')

plt.show()