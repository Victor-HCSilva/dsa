import pandas as pd
import numpy as np

"""Head, tail e sample""""

dsa_df = pd.read_csv("dataset.csv")

"""filtrando as vendas que ocorreram para o segmento de Home offive ou região south"""
#print(dsa_df[(dsa_df.Segmento == "Home office") &  (dsa_df.Regiao == "South") ].head ())

""""Filtrando por uma das condições"""
#print(dsa_df[(dsa_df.Segmento == "Home office") | (dsa_df.Regiao == "South") ].tail ())

"""Filtrando por diferença """
print(dsa_df[(dsa_df.Segmento != "Home office") & (dsa_df.Regiao != "South") ].sample (5))

"""Group By"""
print(dsa_df[[ "Segmento", "Regiao", "Valor_Venda" ]].groupby(["Segmento", "Regiao"]).mean())








