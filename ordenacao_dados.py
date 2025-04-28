import numpy as np
import pandas as pd

dados = {'Nome': ['Maria','Joao', 'Ana', 'Pedro','Joao'],
         'Categoria': ['A', 'B', 'A', 'B', 'B'],
         'Vendas': [100, 200, 150, 250, 350]}

df = pd.DataFrame(dados)
print(df.head())

df_agrupado = df.groupby('Categoria')['Vendas'].sum()
print(df_agrupado)