import pandas as pd 
import matplotlib.pyplot as plt
"""Qual o Total de Vendas Por Data do Pedido?"""
data = pd.read_csv("dataset.csv")

#agrupando por data de pedido, extraindo o valor e somando
df1 = data.groupby("Data_Pedido")["Valor_Venda"].sum()

#grafico
plt.figure(figsize = (20,6))
print(df1)
df1.plot()
plt.show()

