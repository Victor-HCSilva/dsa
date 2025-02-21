import pandas as pd
import numpy as np

dsa_df = pd.read_csv("dataset.csv")

# Encontrando a moda da coluna "Quantidade"
moda = dsa_df["Quantidade"].value_counts().index[0]

# Preenchendo os valores NA (NaN) na coluna "Quantidade"
# Usando a atribuição direta para evitar o FutureWarning
dsa_df["Quantidade"] = dsa_df["Quantidade"].fillna(value = moda)

# Verificando se ainda existem valores ausentes
print(dsa_df.isna().sum())
