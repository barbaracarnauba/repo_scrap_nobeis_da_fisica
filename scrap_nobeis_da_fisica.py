# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 18:32:32 2020

@author: Bárbara Carnaúba
"""
#Lista de Nóbeis da Física

from bs4 import BeautifulSoup
import requests
import pandas as pd

#Webscraping

source=requests.get('https://pt.wikipedia.org/wiki/Laureados_com_o_Nobel_de_F%C3%ADsica')
source.status_code
soup=BeautifulSoup(source.content, 'html.parser') 
print(soup.prettify) 

tab = soup.find("table",{"class":"wikitable"})
print(tab.prettify)

#Passando dados da tabela para um dataframe e exportando para um arquivo xlsx

df = pd.read_html(str(tab))
df2=df[0]
cols = list(df2.columns)
df2 =  df2.rename({cols[3]: 'Laureado', cols[4]: 'País', cols[5]: 'Citação'}, axis='columns')
df2.to_excel('Lista_laureados_nobel_fisica.xlsx',index=False)

#Análise de Dados

# 1) Em quais anos não ouve premiação? R: 1916, 1931, 1934, 1940, 1941, 1942
print(df2.columns.to_list())

df_sem_premiacao=df2[df2['Nº'].str.contains("Não")]

### Agora removemos os anos sem premiação a patir dos índices

df3=df2.drop(index=[20,37,41,49,50,51])

# 2) Que País Ganhou mais prêmios? R: EUA

conta_Paises= df2['País'].value_counts()
dict_conta_paises=dict(conta_Paises)
print(dict_conta_paises)

# 3) Alguém foi laureado mais de uma vez? R: John Bardeen (2)

conta_Laureados=df3['Laureado'].value_counts()
dict_conta_laureados=dict(conta_Laureados)
print(dict_conta_laureados)

dict_maior_ganhador = {k:v for (k,v) in dict_conta_laureados.items() if (v>=2)}
df_maior_ganhador=df3[df3['Laureado']=='John Bardeen']
