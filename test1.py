# task link https://inf-ege.sdamgia.ru/problem?id=1006

import sys

# l - loop, how infinity
l = sys.maxsize

A = [
    [0, 4, l, l, l, l],
    [4, 0, 6, 3, 6, l],
    [l, 6, 0, l, 4, l],
    [l, 3, l, 0, 2, l],
    [l, 6, 4, 2, 0, 5],
    [l, l, l, l, 5, 0]
]

width = len(A)
print('A edge width: ', width)

for k in range(0, width):
    for i in range(0, width):
        for j in range(0, width):
            # print('k: ', k, '\nn: ', i, '\nj: ', j, '\n---------')
            if A[i][k] < l and A[k][j] < l and A[i][j] > A[i][k] + A[k][j]:
                A[i][j] = A[i][k] + A[k][j]

for i in range(0, width):
    print(i)
    for j in range(0, width):
        # print(A[i][j], l)
        if A[i][j] == l:
            A[i][j] = ' '

nodesNames = ['A', 'B', 'C', 'D', 'E', 'F']

print(nodesNames)
for i in range(0, width):
    print(nodesNames[i], A[i])
