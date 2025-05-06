import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x,y, label='Serie 1')

#print(plt.plot(x,y))

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.title('Gráfico de Linhas')

plt.legend()

#print(plt.show())

x = [1,2,3,4,5]
y1 = [2,4,6,8,10]
y2 = [1,3,5,7,9]
y3 = [1,3,7,11,13]

plt.plot(x, y1, label='Série 1')
plt.plot(x, y2, label='Série 2')
plt.plot(x, y3, label='Série 3')

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.title('Gráfico de Múltiplas Linhas')

plt.legend()

#print(plt.show())


dados ={
    'Ano': [2019,2020,2021,2022,2023,2024,2025],
    'Eletrônicos': [100,110,150,130,160,170,180],
    'Vestuário': [80,90,110,100,130,140,120]
}

df_vendas = pd.DataFrame(dados)
#print(df_vendas.head())

anos = df_vendas['Ano']
vendas_eletornicos = df_vendas['Eletrônicos']
vendas_vestuaio = df_vendas['Vestuário']

plt.plot(anos, vendas_eletornicos, label='Eletrônicos', linestyle='--', marker='o')
plt.plot(anos, vendas_vestuaio, label='VEstuários', linestyle='--', marker='>')

plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.title('Comparação de vendas de eletrônicos e vestuários')
plt.legend()
print(plt.show())

