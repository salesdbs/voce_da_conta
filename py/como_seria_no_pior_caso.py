#! /usr/bin/python3.4 k34
import requests
import json

print('\ndeputados iniciando mandato em...')
for ano_mandato in range(2016,2008,-1):
    for mes_mandato in ('01','02','03','04','05','06','07',
                        '08','09','10','11','12'):
        parametros = {  'ordem':'ASC', 
                        'ordenarPor':'nome',
                        'dataInicio':'{ano!s}-{mes!s}-01'.format(ano=ano_mandato
                                                                ,mes=mes_mandato)}
       
        request_lista = requests.get("https://dadosabertos.camara.leg.br/api/v2/deputados"
                                    , params=parametros)
        
        json_data = json.loads(request_lista.text)
        
        print("\n\t",'{ano!s}-{mes}-01'.format(ano=ano_mandato
                                              ,mes=mes_mandato),
                                              len(json_data['dados']))

        arquivo_json = open('./json/{ano!s}-{mes!s}-01@00listaTODOSDeputados.json'.format(ano=ano_mandato,mes=mes_mandato), 'w')
        arquivo_json.write(request_lista.text)
        arquivo_json.close()            
        json_data = json.loads(request_lista.text)
#PEGA DETALHES DE CADA INTERAÇÂO DOS DEPUTADOS
        total_de_deputados = len(json_data['dados'])

        for x in total_de_deputados:
            id_deputado = json_data['dados'][x]['id']
            request_detalhe = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados/{id!s}'.format(id=id_deputado))

            arquivo_detalhe_json = open('./json/{ano!s}-{mes!s}-01@11detalheDeputado_{id}.json'.format(ano=ano_mandato,mes=mes_mandato,id=id_deputado), 'w')
            arquivo_detalhe_json.write(request_detalhe.text)   
            arquivo_detalhe_json.close()