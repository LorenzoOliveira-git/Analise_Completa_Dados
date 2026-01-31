#%%
import pandas as pd
import matplotlib.pyplot as plt

df_limpo = pd.read_csv("../data/df_limpo.csv")

df_limpo.set_index('Unnamed: 0', inplace=True)

df_limpo.index.name = None

#%%

df_limpo['senioridade'].value_counts().plot(kind='bar', title="Frequência por senioridade")

#%%
import seaborn as sns

ordem = ['Executivo','Senior','Pleno','Junior']
sns.barplot(data=df_limpo, x='senioridade', y='usd',order=ordem)
# %%

import matplotlib.pyplot as plt

salario_medio = pd.DataFrame(df_limpo.groupby(["senioridade"])['usd'].mean().sort_values(ascending=False))

plt.figure(figsize=(8,5))
sns.barplot(data=salario_medio, x='senioridade', y='usd')

plt.title('Salário médio por senioridade')
plt.xlabel('senioridade')
plt.ylabel('Salário médio anual (USD)')

plt.show()
# %%


plt.figure(figsize=(8,4))

sns.histplot(df_limpo['usd'], bins=50, kde=True)

plt.title('Salário médio por senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salário médio anual (USD)')

plt.show()
# %%

plt.figure(figsize=(8,5))

sns.boxplot(y=df_limpo['usd'])

plt.title('Salário médio por senioridade')
plt.xlabel('Senioridade')

plt.show()
# %%

plt.figure(figsize=(8,5))

ordem_senioridade = ['Junior','Pleno','Senior','Executivo']

sns.boxplot(x='senioridade',y='usd', data=df_limpo, order=ordem_senioridade)

plt.title('Boxplot da distribuição por senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salário médio anual (USD)')

plt.show()
# %%

plt.figure(figsize=(8,5))

sns.boxplot(x='senioridade',y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2',hue='senioridade')

plt.title('Boxplot da distribuição por senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salário médio anual (USD)')

plt.show()

# %%

import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'browser'

senioridade_media = df_limpo.groupby(['senioridade'])['usd'].mean().sort_values(ascending=False).reset_index()

fig = px.bar(senioridade_media,x='senioridade',y='usd',title='Media Salarial por senioridade',labels={'usd':'Media Salarial Anual (USD)'})

fig.show()

# %%


remoto_contagem = df_limpo.groupby(['remoto'])['usd'].sum().reset_index()

remoto_contagem.columns = ['remoto','Quantidade']

fig = px.pie(remoto_contagem,names='remoto',values='Quantidade',
title='Media Salarial por Periodo de Trabalho')

fig.show()
# %%

fig = px.pie(remoto_contagem,names='remoto',values='Quantidade',
title='Media Salarial por Senioridade',labels={'usd':'Media Salarial Anual (USD)'},
hole=0.5)

fig.update_traces(textinfo='percent+label')
fig.show()
# %%


#DESAFIO: fazer um gráfico que mostre o salário médio de cada país na área de ciência de dados.

import pycountry

def iso2_to_iso3(code):
    try:
        return pycountry.countries.get(alpha_2=code).alpha_3
    except:
        return None
    
df_pais_salario_medio = df_limpo[df_limpo['cargo'] == 'Data Scientist'].groupby(['empresa'])['usd'].mean().reset_index()

df_pais_salario_medio.columns = ["Pais","Media_salarial"]

df_pais_salario_medio["Pais_Iso3"] = df_pais_salario_medio["Pais"].apply(iso2_to_iso3)


fig = px.choropleth(df_pais_salario_medio,locations='Pais_Iso3',
hover_name='Pais',
color='Media_salarial',color_continuous_scale='rdylgn',projection='natural earth',
title='Salário médio de Ciêntista de Dados por país.',
labels={"Media_salarial":"Média dos salários","Pais_Iso3":"País"})

fig.show()

#Vou colocar essa modificação no df_limpo para usar esse campo no app.
df_limpo["Pais_Iso3"] = df_pais_salario_medio["Pais"].apply(iso2_to_iso3)

df_limpo.to_csv("../data/df_limpo.csv")
# %%
