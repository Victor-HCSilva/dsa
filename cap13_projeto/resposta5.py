import pandas as pd
import matplotlib.pyplot as plt

""" 25/02/2025
Qual Segmento Teve o Maior Total de Vendas?
Demonstre o resultado através de um gráfico de pizza.
"""

data = pd.read_csv("dataset.csv")
segmento = data.groupby("Segmento").size()

valores = segmento.values
labels = segmento.index

fig, ax = plt.subplots()
ax.pie(valores, labels=labels, autopct='%1.1f%%')
plt.show()



