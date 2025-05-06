import numpy as np
import pandas as pd

dados = {'Nome': ['Maria','Joao', 'Ana', 'Pedro','Joao'],
         'Categoria': ['A', 'B', 'A', 'B', 'B'],
         'Vendas': [100, 200, 150, 250, 350]}

df = pd.DataFrame(dados)
print(df.head())

print('########################')

df_agrupado = df.groupby('Categoria')['Vendas'].sum()
print(df_agrupado)

print('########################')

#df = df.assign(Ano_Nascimento = lambda x: 2025 - x['Idade'])
#print(df.head())

print('########################')

dados_2 = {'Grupo': ['A', 'B', 'A', 'B'],
           'Valor': [10, 20, 30, 40]}

df = pd.DataFrame(dados_2)
print(df)

print('########################')

df['Media_Grupo'] = df.groupby('Grupo')['Valor'].transform('mean')
print(df.head)