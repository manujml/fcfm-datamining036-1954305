import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# archivo csv local
df = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/csv/SISMOS_MEX_v2.csv')

# concatenar las localizaciones
text = ' '.join(df['Localizacion'].dropna().astype(str).values)

# wordcloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Imagen Word Cloud
plt.figure(figsize=(14, 12))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig("WordCloud_Sismos2023.png")
plt.show()