from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer
import pandas as pd

dados = {
    'A': [1,2,None,4,5],
    'B': [None,2,3,4,5],
    'C': [1,2,3,4,None]
}

df = pd.DataFrame(dados)
#print(df.head())

imputer = SimpleImputer(strategy='mean')

#print('###########')
df_imputer = pd.DataFrame(imputer.fit_transform(df))
#print(df_imputer.head())

