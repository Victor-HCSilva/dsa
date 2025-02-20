#manipulando array de 3 e 4 dimensoes
import numpy as dsa

arr_3d = dsa.array([
    [
        [1,2,3,4],
        [5,6,7,8],
        [1,2,3,4],
    ],
    [
        [1,2,3,4],
        [2,3,4,5],
        [6,7,8,8],
    ]

    ])

#print(arr_3d.ndim)
#print(arr_3d.shape)
#print(arr_3d[0,2,1])#saida: 2



arr_4d = dsa.array([
    [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [1, 2, 3, 4]
        ],
        [
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [6, 7, 8, 8]
        ]
    ],
    [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [1, 2, 3, 4]
        ],
        [
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [6, 7, 8, 8]
        ]
    ]
])

print(arr_4d.shape) #output: (2, 2, 3, 4)
print(arr_4d[0,1,1,0])




