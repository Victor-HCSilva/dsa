#15/02/2025
import numpy as dsa # Pra ficar mais didático!

"""
arr9 = dsa.array([[1,2,3],[4,5,6]])
print("Type:",type(arr9))
#print("Array:",arr9)
"""
arr10 = dsa.ones((2,3))#shape da matriz

#print(arr10)

#lista de listas
lista = [
     [1,2,3],
     [0,7,88],
     [3,-9,-3091],
    ]
#cria uma matriz com a função matrix
arr11 = dsa.matrix(lista)
#print("tipo:",arr11.dtype, '\n',arr11)

# indexação de matrizes:

#print(arr11[2,1])#retorn 9

#print(arr11[0:2,2])#saida 3 88
print(arr11[1,])

#alterando valore 

arr11[1,0] = 100
#print(arr11)

#forcar o tipo de dado:

x = dsa.array([1,2])  #Numpy decide o tipo
y = dsa.array([1.9,0.2])  #Numpy decide o tipo
z = dsa.array([1,2], dtype = dsa.float64)  #Forçamos o tipo do dado

array12 = dsa.array( [ [9,9,3],[19,1,-1,] ], dtype = float)

"""
O ITEMSIZE DE UM ARRAY É UM ATRIBUTO QUE RETORNA O TAMANHO 
EM BYTES DE CADA ELEMENTO DO ARRAY. EM OUTRAS PALAVRAS, O ITEMZISE
REPRESENTA O NUMERO DE BYTES NECESSÁRIOS PARA ARMAZENAR CADA VALOR
DO ARRAY NUMPY
"""

print(array12.itemsize)
print(array12.nbytes)
print(array12.ndim)



























