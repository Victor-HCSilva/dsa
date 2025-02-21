import numpy as np
import pandas as pd 


"""Consultas de dados"""
dsa_df = pd.read_csv("dataset.csv")
#print(dsa_df.Valor_Venda.describe())

"""Consultas (Query) """
dsa_df2 = dsa_df.query("229 > Valor_Venda < 10000")

#print(dsa_df2.Valor_Venda.describe())

dsa_df3 = dsa_df.query(" Valor_Venda > 766")

#print(dsa_df3)







