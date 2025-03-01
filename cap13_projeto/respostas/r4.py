import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sbn

"""Quais São as 10 Cidades com Maior Total de Vendas?"""

data = pd.read_csv("dataset.csv")

df = data.groupby("Cidade")["Valor_Venda"].sum().sort_values(ascending=False)

print(df.head(10))

plt.plot(df.head(10).values)
plt.xticks(rotation=80)
#plt.show()
