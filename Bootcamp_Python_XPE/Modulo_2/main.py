import pandas as pd
import numpy as np

df1 = pd.read_csv('dados_vendas_produtos.csv', encoding='latin1', sep=';')
df2 = pd.read_csv('vendas_produtos_financeiros.csv', encoding='latin1', sep=';')

# Questão 1

#print("Valores ausentes no primeiro dataset:")
#print(df1.isnull().sum())

#print("\nValores ausentes no segundo dataset:")
#print(df2.isnull().sum())

# Questão 2

duplicates = df1.duplicated().sum() + df2.duplicated().sum()
#print(f'Número de registros duplicados: {duplicates}')

# Questão 3

sp_sales = df2[df2['Estado'] == 'SP']
avg_sale_sp = sp_sales['Valor_Total'].mean()
# print(f'Média das vendas em São Paulo: {avg_sale_sp}')

# Questão 4
array = np.array([1, 2, 3, 4])
matrix = array.reshape(-1, 1)
# print(matrix)

# Questão 5
pe_sales = df2[df2['Estado'] == 'PE']
std_quantity_pe = pe_sales['Preco_Unitario'].std()
# print(f'Desvio padrão da quantidade em PE: {std_quantity_pe}')

# Questão 6
df_sc = df2[df2['Estado'] == 'SC']
valor_maximo = df_sc['Valor_Total'].max()

#print(f'O valor máximo da venda para SC é: {valor_maximo}')

#Questão 7
quantidade_por_produto = df2.groupby('Produto')['Quantidade'].sum()
produto_mais_vendido = quantidade_por_produto.idxmax()
quantidade_maxima = quantidade_por_produto.max()

#print(f'O produto mais vendido foi: {produto_mais_vendido} com {quantidade_maxima} unidades vendidas.')

#Questão 8
filtro = (df2['Produto'] == 'Produto 8') & (df2['Estado'] == 'PE')
df_filtrado = df2[filtro]
media_quantidade = df_filtrado['Quantidade'].mean()

#print(f'A média da quantidade vendida do Produto 8 em PE é: {media_quantidade:.2f}')


# Questão 9
filtro = df2['Estado'].isin(['MG', 'SP'])
df2['Valor_Total'] = df2['Valor_Total'].astype(str).str.replace(',', '.').astype(float)
df_filtrado = df2[filtro]
soma_valor_venda = df_filtrado['Valor_Total'].sum()

#print(f'A soma do valor da venda para MG e SP é: {soma_valor_venda:.2f}')

# Questão 10

df2['Valor_Total'] = df2['Valor_Total'].astype(str).str.replace(',', '.').astype(float)

estados_nordeste = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']

df_nordeste = df2[df2['Estado'].isin(estados_nordeste)]

media_valor_total = df_nordeste['Valor_Total'].mean()

print(f'A média do Valor_Total para os estados do Nordeste é: {media_valor_total:.2f}')