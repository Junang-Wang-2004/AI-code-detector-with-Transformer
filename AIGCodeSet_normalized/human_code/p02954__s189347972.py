from itertools import groupby
v1 = list(input())
v2 = [0] * len(v1)
v3 = 0
for v4, v5 in groupby(v1):
    v6, v7 = (v4, len(list(v5)))
    v3 += v7
    if v4 == 'R':
        if v7 % 2 != 0:
            v2[v3 - 1] += v7 // 2 + 1
            v2[v3] += v7 // 2
        else:
            v2[v3 - 1] += v7 // 2
            v2[v3] += v7 // 2
    elif v7 % 2 != 0:
        v2[v3 - v7] += v7 // 2 + 1
        v2[v3 - 1 - v7] += v7 // 2
    else:
        v2[v3 - v7] += v7 // 2
        v2[v3 - 1 - v7] += v7 // 2
print(*v2)
