import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates  as mdates
import datetime

""" 23/02/2025
Qual o Total de Vendas Por Data do Pedido?
Demonstre o resultado através de um gráfico de barras.
"""

data = pd.read_csv("dataset.csv")

data["Data_Pedido"] = pd.to_datetime(data["Data_Pedido"], format="%d/%m/%Y")

vendas_por_datas = data.groupby("Data_Pedido").size()

fig, ax = plt.subplots()

ax.bar(vendas_por_datas.index, vendas_por_datas.values)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%Y"))
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
fig.autofmt_xdate()

plt.xlabel("Data do pedido")
plt.ylabel("Quantid. de vendas")
plt.title("Total de vendas por data do pedido")
plt.tight_layout()
plt.show()
