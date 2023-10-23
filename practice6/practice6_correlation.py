import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/practice2/SISMOS_MEX.csv')

# Había datos que tenían la cadena 'en revision', por lo que se tuvieron que omitir | recordar limpiar y actualizar csv
df = df[~df['Profundidad'].str.contains('en revision', na=False)]
# Convertir a datos numéricos por si las dudas xd
df['Profundidad'] = pd.to_numeric(df['Profundidad'], errors='coerce')

plt.figure(figsize=(24, 20))

# scatter plus linear regression
plt.scatter(df['Magnitud'], df['Profundidad'], alpha=0.5)
sns.regplot(x='Magnitud', y='Profundidad', data=df, scatter=False, color='red', line_kws={"color":"red"})

plt.xlabel('Magnitud')
plt.ylabel('Profundidad')

plt.title('Regresión lineal de Magnitud | Profundidad')

plt.savefig('regression.png')

plt.show()