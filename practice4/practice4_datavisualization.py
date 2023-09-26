import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/practice2/SISMOS_MEX.csv')

# Crea una carpeta imgs para guardar las graficas
if not os.path.exists('imgs'):
    os.makedirs('imgs')

plt.figure(figsize=(40, 36))

gp_localizacion = df.groupby('Localizacion')

for nombre, grupo in gp_localizacion:
    plt.plot(grupo['Fecha'], grupo['Magnitud'], label=nombre)

    plt.xlabel('Fecha')
    plt.ylabel('Magnitud')
    plt.title(f'{nombre}')
    plt.legend()
    plt.savefig(f'imgs/{nombre}.png')
    plt.close()