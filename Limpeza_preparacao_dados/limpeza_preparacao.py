#%%
import pandas as pd

df = pd.read_csv("../data/df_analise.csv")

df.set_index('Unnamed: 0', inplace=True)

df.index.name = None

#Verificação de dados nulo
#Somar todos os valores nulos (que vão estar com True, que é igual a 1, por isso pode somar)
df.isnull().sum()

#Encontrar valores unicos dentro de uma serie
df['ano'].unique()


#Filtro mais direto para descobrir as linhas que tem valores nulos
#any() -> indica que se existir uma valor nulo em QUALQUER coluna (dimensão 1), é para pegar essa linha
df[df.isnull().any(axis=1)]


#Vamos praticar os diversos tipos de modificação de dados nulos

import numpy as np

df_salarios = pd.DataFrame({
    'nome':["Ana","Bruno","Carlos","Daniele"],
    'salario': [4000,np.nan,5000,np.nan]
})

#Substituição de valores nulos pela média de todos os salários
df_salarios["salario_medio"] = df_salarios['salario'].fillna(df_salarios["salario"].mean())

#Substituição de valores nulos pela mediana (muito mais usada com a presença de outliers na sua base de dados) de todos os salários
df_salarios["salario_mediana"] = df_salarios['salario'].fillna(df_salarios["salario"].median())

#Nem todos os valores tem como mudar pela média ou mediana, no caso de temperaturas dos dias é um deles, e nesse caso vamos usar um conceito muito usado no pandas que é o ffill que vai copiar os valores anterios para os valores nan.
df_temperaturas = pd.DataFrame({
    'dia': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex'],
    'temperatura': [30, np.nan, np.nan, 28, 27]
})

#De cima para baixo
df_temperaturas['preenchido_ffill'] = df_temperaturas['temperatura'].ffill()

df_temperaturas

#De baixo para cima
df_temperaturas['preenchido_bfill'] = df_temperaturas['temperatura'].bfill()

df_temperaturas

#Outro caso seria para valores sem a possibilidade de mudar, como variaveis qualitativas, então podemos substituir por um nome fixo.
df_cidades = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'cidade': ['São Paulo', np.nan, 'Curitiba', np.nan, 'Salvador']
})

df_cidades['cidade_corrigida'] = df_cidades['cidade'].fillna('Não informado')

df_cidades

#Removendo as linhas com dados faltantes

df_limpo = df.dropna()

df_limpo.isnull().sum()

#Alterando os tipos de dados

#O método assign serve para atribuir a uma coluna os valores que você colocar como valor. Nesse caso a coluna é ano, e os valores são o df_limpo['ano'].astype('int64').
df_limpo = df_limpo.assign(ano=df_limpo['ano'].astype('Int64'))

df_limpo.to_csv("../data/df_limpo.csv")
     
# %%
