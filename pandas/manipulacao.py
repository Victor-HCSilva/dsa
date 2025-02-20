import pandas as pd
from pandas import DataFrame
#print(pd.__version__)

dados = {
        "Estados":["Santa Catarina","Rio de Janeiro","Paraná","Natal","Porto Alegre","Sergipe"],
        "Ano":[2004,2005,2006,2007,2008,2009],
        "TaxaDesemprego":[1.5,1.0,1.9,1.4,1.2,2]
        }

df = DataFrame(dados)

#print(df.head())

"""Reorganinando Colunas"""
#print(DataFrame(dados, columns = ["Estados","TaxaDesemprego","Ano"]))

"""Adicionando uma nova coluna"""
df2 = DataFrame(
                dados,
                columns = ["Estados","TaxaDesemprego","TaxaCrescimento","Ano"],
                index = ["Estado1","Estado2","Estado3","Estado4","Estado5","Estado6"]
                )

#print(df2)
"""Apenas colunas"""
#print(df2.columns)

"""Apenas valores"""
#print(df2.values)

"""Verificando cada tipo dos dados"""
#print(df2.dtypes)

"""Imprimindo apenas uma coluna"""
coluna_estado = df2["Estados"]
colunas_taxaDesmpregoEAno = df2[["Estados","Ano"]]

#print(coluna_estado)
#print(colunas_taxaDesmpregoEAno)

"""indices do DataFrame"""
#print(df2.index)

"""Apenas a linha com 'Estado3' """
print(df2.filter(items = ["Estado3"], axis = 0))




































