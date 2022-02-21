# task https://inf-ege.sdamgia.ru/problem?id=6172
# question A -> Z min

import sys

l = sys.maxsize

A_names = ['A', 'B', 'C', 'D', 'E', 'F', 'Z',]

A = [
    [0,4,6,l,l,l,46],
    [4,0,1,l,l,l,l],
    [6,1,0,2,l,21,20],
    [l,l,2,0,4,l,l],
    [l,l,l,4,0,2,5],
    [l,l,21,l,2,0,l],
    [46,l,20,l,5,l,0]
]

width = len(A)

for k in range(0, width):
    for i in range(0, width):
        for j in range(0, width):
            if A[i][k] + A[j][k] < A[i][j]:
                A[i][j] = A[i][k] + A[j][k]

for row in A:
    print(row)

