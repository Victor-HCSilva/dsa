import numpy as dsa

""""""
#cria uma matriz com diagonal 0,1,2
array = dsa.diag(dsa.arange(3))
#print(array)

#print(array[1,1])
#print(array[1])
#print(array[:,2])

array1 = dsa.arange(10)

#print(array1[2:9:3])

a = dsa.array([1,2,3,4,5])
b = dsa.array([23,0,5,6,7])

#comparação item a item
#print(a == b)

#comparacao global
#print(dsa.array_equal(a,b))

#maximo valor 
#print(array.max())

#minimo valor
#print(array.min())

#soma + 1 a cada elemento fo array:
#print(dsa.array([1,2,3]) + 1)

#arredondar os valore do array
array4 = dsa.array([
    1.3,3.3,4.1,5.9,0.6,67.5,
    ])

print(dsa.around(array4))


