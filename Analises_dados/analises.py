#%%
import pandas as pd

df = pd.read_csv("../data/salaries.csv")

df.set_index('Unnamed: 0', inplace=True)

df.index.name = None

#Análise geral da base de dados
df.info()

#Descrisão sobre as informações da base de dados, com estátisticas de contagem, média, desvio padrão, valor mínimo, os 3 quartis e o valor máximo.
df.describe()

#Tamanho do DataFrame, em linhas e colunas. Isso é um atributo, e não um método, então não tem parenteses.
df.shape
print(f"linhas: {df.shape[0]}, colunas: {df.shape[1]}")

#Nome das colunas
df.columns

#Renomear as colunas

colunas_pt = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contratacao',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

df.rename(columns=colunas_pt, inplace=True)

#Contar a frequências dos valores categóricos de um DataFrame

df["senioridade"].value_counts()

df["contratacao"].value_counts()

df["remoto"].value_counts()

df["tamanho_empresa"].value_counts()

# Substituir os valores em siglas por valores mais explícitos

substituir_senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}

df['senioridade'] = df["senioridade"].replace(substituir_senioridade)

df['senioridade'].value_counts()

substituir_contrato = {
    'FT': 'Tempo Integral',
    'PT': 'Tempo Parcial',
    'FL': 'Freelancer',
    'CT': 'Contrato'
}

df['contratacao'] = df['contratacao'].replace(substituir_contrato)

df['contratacao'].value_counts()

substituir_tamanho = {
    'M': 'Médio',
    'L': 'Grande',
    'S': 'Pequena'
}

df['tamanho_empresa'] = df['tamanho_empresa'].replace(substituir_tamanho)

df['tamanho_empresa'].value_counts()

substituir_remoto = {
    0: 'Presencial',
    50: 'Hibrido',
    100: 'Remoto'
}

df['remoto'] = df['remoto'].replace(substituir_remoto)

df['remoto'].value_counts()

#Descrição dos dados categoricos

df.describe(include='object')

#Exportar dados para um .csv (pois será usado em outros pacotes)
df.to_csv('../data/df_analise.csv')



# %%
