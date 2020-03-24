#! /usr/bin/python3.4 k34
import os
import json
from pandas import DataFrame, concat

path_dos_json = '/home/chaveiro/compartilhamento/Repositorios/voce_da_conta/py/json'

lista_dos_json = os.listdir(path_dos_json)

lista_dos_json = lista_dos_json[1:3]

lista_dos_json

minha_lista = []

for json_mensal_deputados in lista_dos_json:
    arquivo_json_ = '{path}{json}'.format(path=path_dos_json,json=json_mensal_deputados)
    dados = json.load(open(arquivo_json_))
    df = DataFrame(dados['dados'])
    minha_lista.append(df) 

df = DataFrame(dados['dados'])

df

minha_lista

df3 = concat(minha_lista, ignore_index=False)

df3

id = dados['dados'][1]['id']
id

dados_lista = {}
dados_lista

dados_lista = dados_lista.get(id)
dados_lista

print(dados_lista[])