import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

"""
9 - Qual a Média de Vendas Por Segmento, Por Ano e Por Mês?
Demonstre o resultado através de gráfico de linha
"""
# Carregar os dados
data = pd.read_csv("dataset.csv")

# Converter a coluna 'Data_Pedido' para datetime, especificando o formato
data['Data_Pedido'] = pd.to_datetime(data['Data_Pedido'], format='%d/%m/%Y')

# Calcular a média de vendas por segmento, ano e mês
vendas_por_segmento_ano_mes = data.groupby(['Segmento', data['Data_Pedido'].dt.year, data['Data_Pedido'].dt.month])['Valor_Venda'].mean().unstack(level=0)

# Cores para cada segmento
cores = {'Consumer': 'blue', 'Corporate': 'green', 'Home Office': 'red'}

# Criar o gráfico
fig, ax = plt.subplots(figsize=(15, 7))

# Preparar o eixo x (datas) para o gráfico
datas = pd.to_datetime(vendas_por_segmento_ano_mes.index.get_level_values(0).astype(int).astype(str) + '-' + vendas_por_segmento_ano_mes.index.get_level_values(1).astype(int).astype(str), format='%Y-%m')

# Plotar as linhas para cada segmento
for segmento in vendas_por_segmento_ano_mes.columns:
    ax.plot(datas, vendas_por_segmento_ano_mes[segmento].values, marker='o', linestyle='-', color=cores[segmento], label=segmento)

# Formatar o eixo x para mostrar ano e mês
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())

# Adicionar rótulos e título
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Média de Vendas', fontsize=12)
plt.title('Média de Vendas Por Segmento, Ano e Mês', fontsize=14)

# Adicionar legenda
plt.legend(title='Segmento')

# Mostrar o grid
plt.grid(True)

# Rotacionar os rótulos do eixo x para melhor visualização
plt.xticks(rotation=45)

# Ajustar o layout para evitar cortes
plt.tight_layout()

# Mostrar o gráfico
plt.show()
