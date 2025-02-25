import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("dataset.csv")
data_pedido = data["Data_Pedido"]
valor_venda = data["Valor_Venda"]

data_t = []
valor_t = []
xtick = []

for i in range(len(data_pedido)):
    if(i % 500 == 0):
        data_t.append(data_pedido[i])
        valor_t.append(valor_venda[i])
        xtick.append(i)

plt.plot(data_t,valor_t)
plt.xlabel("Data")
plt.xticks( np.arange(0,len(valor_t)), rotation=45,)
plt.ylabel("Valor($)")
plt.title("Valor X Tempo")
plt.show()