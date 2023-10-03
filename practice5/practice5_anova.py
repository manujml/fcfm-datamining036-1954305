import pandas as pd
import statsmodels.api as smp
from statsmodels.formula.api import ols 

csv = pd.read_csv('C:/Users/Admin/Documents/Documentos Manuel/0. UANL/FCFM/7mo SEMESTRE/Minería de Datos/practice2/SISMOS_MEX.csv')

model = ols ('Magnitud ~ Localizacion', data = csv).fit()

anova = smp.stats.anova_lm(model, typ=2)

if anova["PR(>F)"][0] < 0.005:
    print("Hay diferencias")
    print(anova)
else:
    print(anova)
    print("No hay diferencias")