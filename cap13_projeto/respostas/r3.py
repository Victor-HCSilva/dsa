import matplotlib.pyplot as plt
import pandas as pd
import seaborn as born
""" Qual o Total de Vendas por Estado?
"""

data = pd.read_csv("dataset.csv")
    
df1 = data.groupby("Estado")["Valor_Venda"].sum().reset_index()

plt.figure(figsize=(20,6))
born.barplot(data = df1, y = "Valor_Venda", x =  "Estado")
plt.xticks(rotation=80)
plt.show()
