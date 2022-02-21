# task link https://inf-ege.sdamgia.ru/problem?id=1006

import sys

# l - loop, how infinity
l = sys.maxsize

nodesNames = ['A', 'B', 'C', 'D', 'E', 'F']

A = [
    [0, 4, l, l, l, l],
    [4, 0, 6, 3, 6, l],
    [l, 6, 0, l, 4, l],
    [l, 3, l, 0, 2, l],
    [l, 6, 4, 2, 0, 5],
    [l, l, l, l, 5, 0]
]

width = len(A)
print('A size: ', width, 'x', width)

path = A.copy()

repeats = 0
calculate_repeats = width * width * width

for k in range(0, width):
    for i in range(0, width):
        for j in range(0, width):
            repeats += 1
            print('k:', k, ' i:', i, ' j:', j)
            if A[i][k] + A[k][j] < A[i][j]:
                A[i][j] = A[i][k] + A[k][j]
                path[i][j] = path[i][k]

print('repeats: ', repeats)
print('calculate repeats: ', calculate_repeats)

def shortestPath(i, j):
    if A[i][j] == l:
        print('Path not found')
    else:
        s = i
        while s != j:
            print(nodesNames[s])
            s = path[s][j]
        print(nodesNames[j])

shortestPath(0, 5)

for row in path:
    print(row)

for i in range(0, width):
    for j in range(0, width):
        if A[i][j] == l:
            A[i][j] = ' '

print(nodesNames)
for i in range(0, width):
    print(nodesNames[i], A[i])
print('-----------\n')




