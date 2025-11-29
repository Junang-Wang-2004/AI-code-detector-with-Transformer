import random

def f1(a1):
    v1 = []
    for v2 in range(1, a1 + 1):
        v3 = []
        for v4 in range(1, a1 + 1):
            if v2 != v4 and v4 not in v3:
                v3.append(v4)
        v1.append(v3)
    return v1

def f2(a1):
    v1 = []
    for v2 in range(len(a1)):
        sum = 0
        for v3 in a1[v2]:
            sum += v3
        v1.append(sum)
    return v1

def f3(a1):
    v1 = a1[0]
    for v2 in range(1, len(a1)):
        if a1[v2] != v1:
            return -1
    return v1

def f4():
    v1 = int(input())
    v2 = f1(v1)
    v3 = f2(v2)
    v4 = f3(v3)
    if v4 == -1:
        print('No such graph exists.')
    else:
        print('The graph is simple and connected.')
        print('The sum of the indices of the vertices adjacent to each vertex is', v4)
f4()
