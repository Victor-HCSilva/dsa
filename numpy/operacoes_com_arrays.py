#19/02
import numpy as dsa

#matplotlib + numpy + pandas = ferramenta poderosa para 
#analise de dados!

array = dsa.arange(1,10)

""" Varias funcões da bibiloteca numpy"""
#soma de todos os valores
#print(dsa.sum(array))

#produto dos valores
#print(dsa.prod(array))

#soma acumalada
#print(dsa.cumsum(array))

array1 = dsa.array([[1,2],[3,4]])
array2 = dsa.array([[6,5],[3,5]])

#soma dois arrays
#soma = dsa.add(array1, array2)
#print(soma)

"""Multiplicando duas matrizes"""
#necessário regra básica, A ORDEM DE MULTPLICAÇÃO
#IMPORTA

mult = dsa.dot(array2,array1) # ou mult = array1 @ array2
# ou mesmo dsa.tendordot(array1. array2, axes = ((1),(0)))
print(mult)
