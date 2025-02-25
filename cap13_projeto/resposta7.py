import pandas as pd
import matplotlib.pyplot as plt

""" 23/02/2025
7 - Os gestores da empresa estão considerando conceder diferentes faixas de descontos e
gostariam de fazer uma simulação com base na regra abaixo:
Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
Quantas Vendas Receberiam 15% de Desconto?
"""

data=pd.read_csv("dataset.csv")

valor_venda_maior = data[data["Valor_Venda"] > 1000]["Valor_Venda"]
valor_venda_menor = data[data["Valor_Venda"] < 1000]["Valor_Venda"]

# Aplica os descontos
x = list(map(lambda x: float(x) * 0.85, valor_venda_maior))
x1 = list(map(lambda x: float(x) * 0.90, valor_venda_menor))

# Cria a figura e os subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))  # 1 linha, 2 colunas, tamanho da figura

# Gráfico 1 (vendas maiores que 1000)
ax1.plot(x, label="Desconto de 15%", color="blue")
ax1.set_xlabel("Quant. de vendas")
ax1.set_ylabel("Valores (R$)")
ax1.set_title("Vendas > 1000")
ax1.legend()

# Gráfico 2 (vendas menores que 1000)
ax2.plot(x1, label="Desconto de 10%", color="orange")
ax2.set_xlabel("Quant. de vendas")
ax2.set_ylabel("Valores (R$)")
ax2.set_title("Vendas < 1000")
ax2.legend()

# Ajusta o layout para evitar sobreposição
plt.tight_layout()

# Exibe os gráficos
plt.show()
