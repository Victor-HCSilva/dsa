import pandas as pd
import numpy as np
from pandas import DataFrame
dados = {
        "Estados":["Santa Catarina","Rio de Janeiro","Paraná","Natal","Porto Alegre","Sergipe"],
        "Ano":[2004,2005,2006,2007,2008,2009],
        "TaxaDesemprego":[1.5,1.0,1.9,1.4,1.2,2]
        }


df2 = DataFrame(
                dados,
                columns = ["Estados","TaxaDesemprego","TaxaCrescimento","Ano"],
                index = ["Estado1","Estado2","Estado3","Estado4","Estado5","Estado6"]
                )

"""Resumo estatísco -> apenas valores numéricos"""
#print(df2.describe())

"""Verificando se há valores ausentes no DataFrame"""
#print(df2.isna())

"""Usando o numpy para preencher uma coluna"""
df2["TaxaCrescimento"] = np.arange(6.)
#print(df2.isna())

#print(df2.describe())



