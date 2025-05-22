import pandas as pd
import numpy as np
from PIL.ImageOps import expand
import matplotlib.pyplot as plt
import seaborn as sns

########## Tratando dados do arquivo 1

df1 = pd.read_csv("clientes_caracteristicas_fisicas.csv", header=None, names=[
    "ID Cliente", "Cor do Cabelo", "Cor dos Olhos", "Cor da Pele",
    "Altura (cm)", "Peso (kg)", "Tatuagens", "Piercings", "Tipo Sanguíneo", "Tipo de Pele"
], na_values=["...", " ", "NaN"], engine="python", on_bad_lines="warn")

df1["Tipo Sanguíneo"] = df1["Tipo Sanguíneo"].str.replace(r"\.+", "", regex=True)
df1["Tipo de Pele"] = df1["Tipo de Pele"].str.replace(r"\.+", "", regex=True)

cores_pele_validas = ["Negra", "Branca", "Parda", "Indígena", "Amarela"]
tipos_sanguineos_validos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
tipos_pele_validos = ["Mista", "Oleosa", "Seca"]

# Corrigir "Cor da Pele"
df1["Cor da Pele"] = df1["Cor da Pele"].str.strip().str.capitalize()
df1["Cor da Pele"] = df1["Cor da Pele"].apply(
    lambda x: x if x in cores_pele_validas else np.nan
)

# Corrigir "Tipo Sanguíneo"
df1["Tipo Sanguíneo"] = df1["Tipo Sanguíneo"].str.strip().str.upper()
df1["Tipo Sanguíneo"] = df1["Tipo Sanguíneo"].apply(
    lambda x: x if x in tipos_sanguineos_validos else np.nan
)

# Corrigir "Tipo de Pele"
df1["Tipo de Pele"] = df1["Tipo de Pele"].str.strip().str.capitalize()
df1["Tipo de Pele"] = df1["Tipo de Pele"].apply(
    lambda x: x if x in tipos_pele_validos else np.nan
)

df1["Altura (cm)"] = pd.to_numeric(df1["Altura (cm)"], errors="coerce")
df1["Peso (kg)"] = pd.to_numeric(df1["Peso (kg)"], errors="coerce")
df1["Tatuagens"] = pd.to_numeric(df1["Tatuagens"], errors="coerce").astype("Int64")
df1["Piercings"] = pd.to_numeric(df1["Piercings"], errors="coerce").astype("Int64")

# Remover outliers (ex.: IMC entre 15 e 50)
df1["IMC"] = df1["Peso (kg)"] / (df1["Altura (cm)"] / 100) ** 2
df1 = df1[(df1["IMC"] >= 15) & (df1["IMC"] <= 50)].drop(columns="IMC")

df1["Cor da Pele"] = df1["Cor da Pele"].fillna(df1["Cor da Pele"].mode()[0])
df1["Tipo Sanguíneo"] = df1["Tipo Sanguíneo"].fillna(df1["Tipo Sanguíneo"].mode()[0])
df1["Tipo de Pele"] = df1["Tipo de Pele"].fillna(df1["Tipo de Pele"].mode()[0])

# Preencher numéricos com a mediana
df1["Altura (cm)"] = df1["Altura (cm)"].fillna(df1["Altura (cm)"].median())
df1["Peso (kg)"] = df1["Peso (kg)"].fillna(df1["Peso (kg)"].median())

df1 = df1.drop_duplicates(subset="ID Cliente", keep="first")

############## Tratando dados do arquivo 2

df2 = pd.read_csv('clientes_informacoes_demograficas.csv', encoding='utf-8', sep=';', decimal='.')
df2.columns = [
    "ID Cliente", "Escolaridade", "Tem Filhos", "Salário", "Idade",
    "Estado", "Estado Civil", "Profissão", "Hobbies (Código)", "Número de Cartões de Crédito"
]

ESCOLARIDADE_VALIDA = ["Fundamental", "Médio", "Superior", "Pós-Graduação"]
ESTADO_CIVIL_VALIDO = ["Solteiro", "Casado", "Divorciado", "Viúvo"]
PROFISSAO_VALIDA = ["Professor", "Empesário", "Médico", "Advogado", "Engenheiro", "Artista", "Outros"]

# Padronizar Valores DF2
df2["Escolaridade"] = df2["Escolaridade"].str.strip().str.capitalize()
df2["Escolaridade"] = df2["Escolaridade"].replace({"Pos-Graduacao": "Pós-Graduação"})
df2["Escolaridade"] = df2["Escolaridade"].apply(
    lambda x: x if x in ESCOLARIDADE_VALIDA else np.nan
)

df2["Estado Civil"] = df2["Estado Civil"].str.strip().str.capitalize()
df2["Estado Civil"] = df2["Estado Civil"].apply(
    lambda x: x if x in ESTADO_CIVIL_VALIDO else np.nan
)

df2["Profissão"] = df2["Profissão"].str.strip().str.capitalize()
df2["Profissão"] = df2["Profissão"].apply(
    lambda x: x if x in PROFISSAO_VALIDA else np.nan
)

df2["Idade"] = df2["Idade"].fillna(df2["Idade"].median())
df2 = df2[(df2["Salário"] > 0) & (df2["Idade"].between(18,100))]

ESTADOS_VALIDOS = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
                   "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
                   "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

df2["Estado"] = df2["Estado"].str.strip().str.upper()
df2["Estado"] = df2["Estado"].apply(
    lambda x: x if x in ESTADOS_VALIDOS else np.nan
)

df2["Escolaridade"] = df2["Escolaridade"].fillna(df2["Escolaridade"].mode()[0])
df2["Estado Civil"] = df2["Estado Civil"].fillna(df2["Estado Civil"].mode()[0])
df2["Estado"] = df2["Estado"].fillna(df2["Estado"].mode()[0])



df2["Hobbies (Código)"] = df2["Hobbies (Código)"].str.strip().str.upper()

#print(df2.head())
#print("\nResumo dos Dados tratados:")
#print(df2.info())

# Questão 1
hobbies_quantidades = df2["Hobbies (Código)"].nunique()
#print(f"Quantidade de códigos de hobbies distintos: {hobbies_quantidades}")

# Questão 2
cores_de_cabelo = df1['Cor do Cabelo'].value_counts().idxmax()
#print(cores_de_cabelo)

# Questão 3
correlacao_altura_peso = df1[['Altura (cm)', 'Peso (kg)']].corr()
#print(correlacao_altura_peso)

# Questão 4
estado_maior_salario = df2.groupby("Estado")["Salário"].mean().sort_values(ascending=False)
#print(estado_maior_salario)

# Questão 5

plt.figure(figsize=(10, 6))
plt.hist(df2["Idade"], bins=30, edgecolor='black')
plt.title("Distribuição da Idade dos Clientes")
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.grid(True)
#plt.show()

# Questão 6
proporcao_tatuagens = (df1["Tatuagens"] > 0).mean()
proporcao_piercings = (df1["Piercings"] > 0).mean()

#print(f"Proporção de clientes com tatuagens: {proporcao_tatuagens:.2f}")
#print(f"Proporção de clientes com piercings: {proporcao_piercings:.2f}")

# Questão 7
df2["SalarioAcima5000"] = df2["Salário"] > 5000

# Calcula a proporção por estado
proporcoes = df2.groupby("Estado")["SalarioAcima5000"].mean()

# Ordena para encontrar o estado com a maior proporção
estado_top = proporcoes.sort_values(ascending=False).head(1)

#print("Estado com maior proporção de salários > R$ 5000:")
#print(estado_top)

# Questão 8



#Questão 9


# Questão 11
df_superior = df2[df2["Escolaridade"] == "Superior"]
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_superior["Salário"], color="skyblue")
plt.title("Distribuição de Salários - Escolaridade Superior")
plt.xlabel("Salário (R$)")
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df_superior["Salário"], kde=True, color="teal", bins=20)
plt.title("Distribuição de Salários - Escolaridade Superior")
plt.xlabel("Salário (R$)")
plt.ylabel("Frequência")
plt.grid(linestyle="--", alpha=0.7)
plt.show()
