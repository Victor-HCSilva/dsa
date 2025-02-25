import pandas as pd
import matplotlib.pyplot as plt

""" 23/02/2025
6 - Qual o Total de Vendas Por Segmento e Por Ano?
"""


data = pd.read_csv("dataset.csv")

vendas_por_estado_e_ano = data.groupby('Valor_Venda')
vendas_por_estado_e_ano = data.groupby("Segmento").size()

print(vendas_por_estado_e_ano.head())

# Criar o gráfico de barras
fig, ax = plt.subplots()  # Cria uma figura e um eixo explicitamente
ax.bar(vendas_por_estado_e_ano.index, vendas_por_estado_e_ano.values)  # Corrigido aqui

# Labels e título
plt.ylabel("Valores")
plt.xlabel("Segmentos")
plt.title("Total de Vendas X Segmento/anos")
plt.tight_layout()

# Exibir o gráfico
plt.show()

