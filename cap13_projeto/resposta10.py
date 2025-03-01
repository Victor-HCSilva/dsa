import pandas as pd
import matplotlib.pyplot as plt

"""
Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12
SubCategorias?
"""

# Ler o arquivo CSV
data = pd.read_csv("dataset.csv")
filtro = ["Valor_Venda", "Categoria", "SubCategoria"]

#12 maiores
data = data[filtro]
data = data["Valor_Venda"].nlargest(12)

plt.plot(data.values)

plt.show()



