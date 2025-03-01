import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
data = pd.read_csv("dataset.csv")

# Agrupar por 'Estado' e contar as vendas
vendas_por_estado = data.groupby('Estado').size()

# Criar o gráfico de barras
fig, ax = plt.subplots() 
ax.bar(vendas_por_estado.index, vendas_por_estado.values)  

# Labels e título
plt.ylabel("Quant. de Vendas")
plt.xlabel("Estado")
plt.title("Total de Vendas Por Estado")
plt.tight_layout()

# Exibir o gráfico
plt.show()
