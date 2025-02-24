import pandas as pd
import matplotlib.pyplot as plt
""" 23/02/2025
Qual o Total de Vendas por Estado?
Demonstre o resultado através de um gráfico de barras.
"""
# Ler o arquivo CSV
data = pd.read_csv("dataset.csv")

# Agrupar por 'Estado' e contar as vendas
vendas_por_estado = data.groupby('Estado').size()

# Criar o gráfico de barras
fig, ax = plt.subplots()
ax.bar(vendas_por_estado.index, vendas_por_estado.values)

# Definir quais rótulos exibir (ex: a cada 3 estados)
n = 3  # Exibir a cada 3 estados
tick_locations = range(0, len(vendas_por_estado.index), n)
tick_labels = vendas_por_estado.index[tick_locations]

# Definir os ticks e rótulos no eixo x
ax.set_xticks(tick_locations)
ax.set_xticklabels(tick_labels)

# Labels e título
plt.ylabel("Quant. de Vendas")
plt.xlabel("Estado")
plt.title("Total de Vendas Por Estado")
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos
plt.tight_layout()

# Exibir o gráfico
plt.show()
