#!/usr/bin/env python
# coding: utf-8

# In[1]:


#! /usr/bin/python3.4 k34
import os
import json
from pandas import DataFrame, concat


# In[2]:


path_dos_json = '/home/chaveiro/0-repositorios/dadosAbertos/acesso_API/deputados/json/'


# In[24]:


lista_dos_json = os.listdir(path_dos_json)


# In[22]:


#lista_dos_json


# In[25]:


lista_dos_json = lista_dos_json[1:3]


# In[26]:


lista_dos_json


# In[97]:


minha_lista = []


# In[98]:


for json_mensal_deputados in lista_dos_json:
    arquivo_json_ = '{path}{json}'.format(path=path_dos_json,json=json_mensal_deputados)
    dados = json.load(open(arquivo_json_))
    df = DataFrame(dados['dados'])
    minha_lista.append(df) 


# In[99]:


df = DataFrame(dados['dados'])


# In[100]:


df


# In[101]:


minha_lista


# In[104]:


df3 = concat(minha_lista, ignore_index=False)


# In[105]:


df3


# In[80]:


#df['id'].unique().tolist()
#df['id'].unique()
#ddd = {df['nome'].unique():df['id'].unique()}


# In[62]:


id = dados['dados'][1]['id']
id


# In[63]:


dados_lista = {}
dados_lista


# In[64]:


dados_lista = dados_lista.get(id)
dados_lista


# In[68]:


print(dados_lista[])


# In[45]:


dados_lista = dados_lista.popitem{}
dados_lista


# In[82]:


lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']


# In[ ]:




