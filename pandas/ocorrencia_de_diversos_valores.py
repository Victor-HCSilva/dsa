import pandas as pd
import numpy as np

dsa_df = pd.read_csv("dataset.csv")

#print(dsa_df.shape)

"""Outro método para filtros, se um ou mais valore são encontrados em uma coluna"""
#print(dsa_df[dsa_df["Quantidade"].isin([5,7,9,11])])
#print(dsa_df[dsa_df["Quantidade"].isin([5,7,9,11])].shape)

"""Apenas os 10 primeiros items filtrados"""
print(dsa_df[dsa_df["Quantidade"].isin([5,7,9,11])][:10])
