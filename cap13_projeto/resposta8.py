import pandas as pd
import matplotlib.pyplot as plt

"""Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior. Qual
Seria a Média do Valor de Venda Antes e Depois do Desconto?
"""

data=pd.read_csv("dataset.csv")

valor_venda_maior = data[data["Valor_Venda"] > 1000]["Valor_Venda"]
valor_venda_menor = data[data["Valor_Venda"] < 1000]["Valor_Venda"]

# Aplica os descontos
x = list(map(lambda x: float(x) * 0.85, valor_venda_maior))
x1 = list(map(lambda x: float(x) * 0.90, valor_venda_menor))

#É em dolares mais quero deixar com reais :)
print(f"Antes do desconto: R${valor_venda_maior.values.mean():.4f}")
print(f"Depois do desconto(15%): R${sum(x)/len(x):.4f}")


