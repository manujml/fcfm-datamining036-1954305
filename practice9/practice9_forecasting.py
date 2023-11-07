import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Cargar el archivo CSV
data = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/csv/SISMOS_MEX_v2.csv')

# Convertir la columna 'Fecha' a tipo datetime
data['Fecha'] = pd.to_datetime(data['Fecha'])