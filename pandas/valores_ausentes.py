import pandas as pd
import numpy as np
from slicing import df2
dsa_df = pd.read_csv("dataset.csv")

#print(dsa_df.head(5))
#print(dsa_df.isna().sum())

"""Extaindo a moda da coluna Quantity"""
moda = dsa_df["Quantidade"].value_counts().index[0]

print(moda)


