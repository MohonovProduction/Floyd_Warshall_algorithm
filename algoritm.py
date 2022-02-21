# task link https://inf-ege.sdamgia.ru/problem?id=1006

import sys

# l - loop, how infinity
l = sys.maxsize

A_names = ['A', 'B', 'C', 'D', 'E', 'F']

A = [
    [0, 4, l, l, l, l],
    [4, 0, 6, 3, 6, l],
    [l, 6, 0, l, 4, l],
    [l, 3, l, 0, 2, l],
    [l, 6, 4, 2, 0, 5],
    [l, l, l, l, 5, 0]
]

width = len(A)
print('A size: ', width, 'x', width, '\n')

path = A.copy()

for k in range(0, width):
    for i in range(0, width):
        for j in range(0, width):
            print('k:', k, ' i:', i, ' j:', j)
            if A[i][k] + A[k][j] < A[i][j]:
                A[i][j] = A[i][k] + A[k][j]
                path[i][j] = path[i][k]

def shortestPath(i, j):
    if A[i][j] == l:
        print('\nPath not found')
    else:
        print('\nshortest path:')
        s = i
        while s != j:
            print(A_names[s])
            s = path[s][j]
        print(A_names[j], '\n')

shortestPath(0, 5)

for i in range(0, width):
    for j in range(0, width):
        if A[i][j] == l:
            A[i][j] = ' '

print(A_names)
for i in range(0, width):
    print(A_names[i], A[i])
print('-----------\n')




