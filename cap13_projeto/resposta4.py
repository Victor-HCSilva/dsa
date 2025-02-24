import pandas as pd
import matplotlib.pyplot as plt

""" 23/02/2024
Quais São as 10 Cidades com Maior Total de Vendas?
Demonstre o resultado através de um gráfico de barras.
"""

def top_10_vendas_por_estado(df, coluna_estado='Estado', coluna_vendas='Valor_Venda'):
    """
    Seleciona as colunas de estado e vendas, calcula o total de vendas por estado,
    identifica os 10 maiores e exibe um gráfico de barras.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados.
        coluna_estado (str): Nome da coluna com os nomes dos estados.
        coluna_vendas (str): Nome da coluna com os valores de vendas.

    Returns:
        None (exibe o gráfico)
    """

    # 1. Selecionar as colunas relevantes
    df_selecionado = df[[coluna_estado, coluna_vendas]].copy()

    # 2. Agrupar por estado e somar as vendas
    vendas_por_estado = df_selecionado.groupby(coluna_estado)[coluna_vendas].sum()

    # 3. Encontrar os 10 maiores valores de vendas
    top_10 = vendas_por_estado.nlargest(10)

    # 4. Criar o gráfico
    plt.figure(figsize=(12, 6))  # Ajuste o tamanho conforme necessário
    top_10.plot(kind='bar', color='skyblue')
    plt.title('Top 10 Estados por Vendas')
    plt.xlabel('Estado')
    plt.ylabel('Total de Vendas')
    plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos para melhor legibilidade
    plt.tight_layout()  # Ajusta o layout para evitar cortes
    plt.show()

# Exemplo de uso (crie um DataFrame de exemplo se não tiver um)
data = pd.read_csv("dataset.csv")

df = pd.DataFrame(data)

top_10_vendas_por_estado(df)
