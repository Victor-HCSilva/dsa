import numpy as dsa
"""flateen() - > achatar"""
array = dsa.array([[1,2,3,4],[2,3,4,5]])
#print(array.flatten())

array1 = dsa.array([1,2,4])

#repetir array:
print(dsa.repeat(array1,3))
print(dsa.tile(array1,3))

#copiar array - Bom para backup
copia = dsa.copy(array)



