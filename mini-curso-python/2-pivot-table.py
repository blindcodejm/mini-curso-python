import pandas as pd 

#1 Importando dados
data = pd.read_excel("data/vendacarros.xlsx")
# print(data)

#1.1 olocando o comando abaixo o python mostra qual o tipo de daos ele esta retornando
# nome = "Jonas"
# print(type(nome))

#2 Selecionando colunas especificas do dataframe(basicamente criamos uma array bidimensional com os componestes desejados)
df = data[["Fabricante", "ValorVenda", "Ano"]]
print(df)

#3 Criadno a tabela pivot
pivot_table = df.pivot_table(
  index="Ano",
  columns="Fabricante",
  values="ValorVenda",
  aggfunc="sum"
)

print(pivot_table)

#4 Exportando tabela pivot em arquivo excel
pivot_table.to_excel("data/pivot_table.xlsx", "relatorio")