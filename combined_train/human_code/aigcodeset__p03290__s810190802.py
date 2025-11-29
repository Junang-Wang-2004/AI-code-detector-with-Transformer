import random
import bisect
import math
v1 = 0
v2 = 0
iter = 2
v3 = 50
v4 = 1000
v5 = 1
v6 = 0
v7, v8 = [int(i) for v9 in input().split()]
v10 = [0 for v9 in range(v7)]
v11 = [0 for v9 in range(v7)]
for v9 in range(v7):
    v10[v9], v11[v9] = [int(v9) for v9 in input().split()]
v12 = [v10[v9] * (v9 + 1) * 100 + v11[v9] for v9 in range(v7)]

def f1(a1):
    v1 = sum([v10[v9] * a1[v9] for v9 in range(v7)])
    v2 = sum([v12[v9] * a1[v9] for v9 in range(v7)])
    v3 = -1
    for v4 in range(v7):
        if a1[v7 - 1 - v4] == 0:
            v3 = v7 - 1 - v4
            break
    if v3 != -1:
        for v4 in range(v10[v3]):
            if v8 > v2:
                v1 += 1
                v2 += (v3 + 1) * 100
            else:
                break
    if v8 > v2:
        v1 = 10000
    return v1

def f2(a1, a2, a3, a4):
    v1 = [1 if random.uniform(0, 1) < 1 / (1 + math.e ** (-a2[v9])) else 0 for v9 in range(v7)]
    return v1

def f3(a1, a2, a3, a4, a5, a6=1.0, a7=2.0, a8=0.75):
    v1 = a7 + a8
    v2 = 2 / abs(2 - v1 - (v1 * v1 - 4 * v1) ** 0.5)
    if v1 != 0:
        v3 = [v2 * (a5 * a2[v9] + a7 * random.uniform(0, a6) * (a3[v9] - a1[v9]) + a8 * random.uniform(0, a6) * (a4[v9] - a1[v9])) for v9 in range(v7)]
    else:
        v3 = [a5 * a2[v9] + a7 * random.uniform(0, a6) * (a3[v9] - a1[v9]) + a8 * random.uniform(0, a6) * (a4[v9] - a1[v9]) for v9 in range(v7)]
    return v3

def f4():
    v1 = 1.0
    v2, v3 = (1.25, 0.25)
    v4 = [v6 for v9 in range(v7)]
    v5 = [v5 for v9 in range(v7)]
    v6 = [[random.randint(v4[j], v5[j]) for v7 in range(v7)] for v9 in range(v3)]
    v8 = [[0.0 for v7 in range(v7)] for v9 in range(v3)]
    v9 = v6[:]
    v10 = [f1(p) for v11 in v6]
    if v2 == 1:
        v12 = v10.index(max(v10))
    elif v2 == 0:
        v12 = v10.index(min(v10))
    v13 = v9[v12][:]
    for v14 in range(v4):
        for v15 in range(v3):
            v16 = v6[v15][:]
            v17 = v8[v15][:]
            v11 = v9[v15][:]
            if v1 >= 2:
                v18 = sorted(v9)
                v19 = bisect.bisect_left(v18, v11) + 1
                v1 = v2 - v19 * (v2 - v3) / (v3 - 1)
            v20 = f2(v16, v17, v4, v5)
            v6[v15] = v20[:]
            v21 = f3(v20, v17, v11, v13, v1)
            v8[v15] = v21[:]
            v22 = f1(v20)
            if v2 == 1:
                if v22 > v10[v15]:
                    v10[v15] = v22
                    v9[v15] = v20[:]
            elif v2 == 0:
                if v22 < v10[v15]:
                    v10[v15] = v22
                    v9[v15] = v20[:]
        if v2 == 1:
            v12 = v10.index(max(v10))
            v13 = v9[v12][:]
        elif v2 == 0:
            v12 = v10.index(min(v10))
            v13 = v9[v12][:]
        f.write(str(max(v10)) + '\n')
    if v2 == 1:
        return max(v10)
    elif v2 == 0:
        return min(v10)
with open('test_' + str(v1) + '.txt', 'w') as v13:
    if v2 == 1:
        v14 = -float('inf')
        for v9 in range(iter):
            v14 = max(v14, f4())
    elif v2 == 0:
        v14 = float('inf')
        for v9 in range(iter):
            v14 = min(v14, f4())
print(v14)
