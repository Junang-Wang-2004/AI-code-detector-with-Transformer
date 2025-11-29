v1, v2, v3 = map(int, input().split())
v4 = [list(map(int, input().strip())) for v5 in range(v1)]
from copy import deepcopy
v6 = deepcopy(v4)
for v5 in range(v1):
    for v7 in range(v2 - 1):
        v6[v5][v7 + 1] += v6[v5][v7]

def f1(a1):
    v1 = []
    v2 = [0]
    for v3 in range(v1 - 1):
        if a1[v3] == 1:
            v1.append(v2)
            v2 = [v3 + 1]
        else:
            v2.append(v3 + 1)
    v1.append(v2)
    return v1

def f2(a1):
    for v1 in range(v1 - 1):
        if a1[v1] == 0:
            a1[v1] = 1
            for v2 in range(0, v1):
                a1[v2] = 0
            break
    return a1

def f3(a1, a2, a3):
    v1 = 0
    for v2 in a1:
        if a2 != 0:
            v1 = v1 + v6[v2][a3 - 1] - v6[v2][a2 - 1]
        else:
            v1 += v6[v2][a3 - 1]
    return v1

def f4(a1, a2):
    v1 = 0
    for v2 in a1:
        v1 += v4[v2][a2]
    if v1 > v3:
        return False
    else:
        return True
v8 = v1 + v2 - 2
v9 = [0] * (v1 - 1)
for v5 in range(2 ** (v1 - 1)):
    v10 = 0
    v11 = 0
    v12 = 0
    v13 = f1(v9)
    for v7 in range(1, v2):
        v14 = 0
        for v15 in v13:
            if f3(v15, v11, v7 + 1) > v3:
                if f4(v15, v11) == False:
                    v10 = 1
                    break
                else:
                    v14 = 1
        if v10 == 1:
            break
        if v14 == 1:
            v12 += 1
            v11 = v7
    if f4(v15, v2 - 1) == True:
        v8 = min(v8, v12 + sum(v9))
    f2(v9)
print(v8)
