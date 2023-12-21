import pandas as pd 

#1 Importando dados
data = pd.read_excel("data/vendacarros.xlsx")
print(data)

#2 Lista os 5 primeiros registros por padrão ou conforme o numero colocado
print(data.head())

#3 Lista os 5 ultimos registros por padrão ou conforme o numero colocado
print(data.tail())

#4 Contagem de valores por fabricante
print(data['Fabricante'].value_counts())
