import pandas as pd
import matplotlib.pyplot as iplt
import numpy as np

"""Qual Segmento Teve o Maior Total de Vendas?"""

data =  pd.read_csv("dataset.csv")

df = data.groupby("Segmento")["Valor_Venda"].sum().reset_index().sort_values(by="Valor_Venda")

print(type(df.values))

#x = [i[0] for i in df.values]
#y = 
#plt.pie(df.values, labels=["q","c","d"], autopct='%1.1f%%')
#plt.show()
