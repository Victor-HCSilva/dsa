import numpy as dsa
import matplotlib.pyplot as plt

filename = "dataset.csv"

try:
    # Ler as colunas 0, 1 e 2
    arr13 = dsa.loadtxt(filename, delimiter=',', usecols=(0, 1, 2), skiprows=1)
    print(arr13)
    print(type(arr13))

    # Ler as colunas 0 e 1 separadamente
    var1, var2 = dsa.loadtxt(filename, delimiter=',', usecols=(0, 1), skiprows=1, unpack=True)

    # Criar o gráfico de dispersão
    plt.plot(var1, var2, 'o', markersize=6, color='red')

    # Adicionar rótulos aos eixos e um título
    plt.xlabel("Variável 1 (Coluna 0)")
    plt.ylabel("Variável 2 (Coluna 1)")
    plt.title("Gráfico de Dispersão das Variáveis 1 e 2")

    # Exibir o gráfico
    plt.show()

except FileNotFoundError:
    print(f"Erro: Arquivo '{filename}' não encontrado.")
except ValueError as e:
    print(f"Erro de valor ao ler o arquivo: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
