import pandas as pd
import matplotlib.pyplot as plt

"""Qual Cidade com Maior Valor de Venda de Produtos 
da Categoria 'Office Supplies'?
"""
data = pd.read_csv("dataset.csv")
filtro = data["Categoria"] == "Office Supplies"

#aplicação do filtro
df1 = data[filtro]

#Agrupando por cidade e calculando o valor total de valor_venda
df2 = df1.groupby("Cidade")["Valor_Venda"].sum()

maior_valor = df2.idxmax()

print(f"Maior valor: {maior_valor}")
print(df2.sort_values(ascending=False))






