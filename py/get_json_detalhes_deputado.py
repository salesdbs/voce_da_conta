#! /usr/bin/python3.4 k34
import os
import json
import sqlalchemy
from pandas import DataFrame, concat

path_dos_json = '/home/chaveiro/0-repositorios/dadosAbertos/acesso_API/deputados/json/'
lista_dos_json = os.listdir(path_dos_json)
minha_lista = []
for json_mensal_deputados in lista_dos_json:
    arquivo_json_ = '{path}{json}'.format(path=path_dos_json,json=json_mensal_deputados)
    dados = json.load(open(arquivo_json_))
     
    for id_deputado in range(0,len(dados['dados'])):
        dados['dados'][id_deputado].update({'data_periodo':arquivo_json_[69:79]})

    df = DataFrame(dados['dados'])
    minha_lista.append(df)

dataFrame_Deputados = concat(minha_lista, ignore_index=False)

dataFrame_Deputados.id.unique()

arquivo_json = open('lista.csv', 'w')
arquivo_json.write(request_lista.text)
arquivo_json.close()

#arquivos = [arq for arq in arquivo_json if os.path.isfile(arq)]
#Tenho que pegar: id_deputado = json_data['dados'][x]['id']

"""
#PARTE DO BANCO

# Connect to database (Note: The package psychopg2 is required for Postgres to work with SQLAlchemy)
engine = sqlalchemy.create_engine("postgresql://postgres:Postgres2018!@localhost/DBclass_awareness")
con = engine.connect()

# Verify that there are no existing tables
print(engine.table_names())

table_name = 'deputados'
dataFrame_Deputados.to_sql(table_name, con, if_exists='append',)
print(engine.table_names())

"""