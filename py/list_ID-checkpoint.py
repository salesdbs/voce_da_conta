# coding: utf-8

# In[1]:


#! /usr/bin/python3.4 k34
import os
import json
import requests
import sqlalchemy
from pandas.io.json import json_normalize 
from pandas import DataFrame, concat, Series, get_dummies


# In[2]:


#Colocar o endereço da pasta em que se encontra os JSON dos deputados.
path_dos_json = '/home/chaveiro/compartilhamento/Repositorios/voce_da_conta/'
#path_dos_json = './json/'


# In[3]:


#PARTE DO BANCO

# Connect to database (Note: The package psychopg2 is required for Postgres to work with SQLAlchemy)
engine = sqlalchemy.create_engine("postgresql://postgres:Postgres2018!@localhost/DBclass_awareness")
con = engine.connect()


# In[4]:


lista_dos_json = os.listdir(path_dos_json)
#lista_dos_json = lista_dos_json[1:3]


# In[13]:


minha_lista = []
lista_dos_json


# In[6]:


for json_mensal_deputados in lista_dos_json:
    arquivo_json_ = '{path}{json}'.format(path=path_dos_json,json=json_mensal_deputados)
    dados = json.load(open(arquivo_json_))

    print(dados['dados'][0], dados['dados'][1], dados['dados'][540], sep='\n\n',end='\n\n====>\n')

    for id_deputado in range(0,len(dados['dados'])):
        dados['dados'][id_deputado].update({'data_periodo':arquivo_json_[69:79]})

    print(dados['dados'][0], dados['dados'][1], dados['dados'][540], sep='\n\n',end='\n\n====>\n')

    df = DataFrame(dados['dados'])
    minha_lista.append(df) 


# In[7]:


df3 = concat(minha_lista, ignore_index=False)


# In[8]:


#PARTE DO BANCO
#table_name = 'deputados'
##df3.to_sql(table_name, con, if_exists='append',)
print(engine.table_names())


# In[9]:


#df['id'].unique().tolist()
#df['id'].unique()
#ddd = {df['nome'].unique():df['id'].unique()}


#Linhas 0 até o 2 da coluna 0:
df3.iloc[0:5,3]


# In[12]:


len(df3.id.unique())
#df3.id.unique()[1:3]


# In[17]:


detalhe_deputados = []
for id in df3.id.unique():#df3.id.unique()[1:3]:
    print(id)
#Detalhe do deputado:
    request_detalhe = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados/{id!s}'.format(id=id))
    json_detalhe = json.loads(request_detalhe.text)
    df_detalhado = json_normalize(json_detalhe['dados'])
    detalhe_deputados.append(df_detalhado) 
#Solicitação de reembolso do deputado:
    #vai ser aqui....


# In[20]:


dicionario_deputados_detalhe = concat(detalhe_deputados, ignore_index=False,sort=True)
dicionario_deputados_detalhe


# In[21]:


print(engine.table_names())


# In[22]:


#GRAVA OS DETALHES DOS DEPUTADOS
"""
table_name = 'deputados_detalhes'
dicionario_deputados_detalhe.to_sql(table_name, con, if_exists='append',)
print(engine.table_names())
"""


# In[23]:


exit()


# In[ ]:


#df3.nome.find('Câmera')
df3.sort_values(["data_periodo", "nome"], axis=0, 
                 ascending=True, inplace=True) 
df3.loc[df3['nome'].str.contains('SILAS CÂMARA')].head(2)

