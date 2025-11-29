import sys
v1 = int(input())
v2 = [[(int(x), True) for v3 in input().split()] for v4 in range(v1)]
v5 = 0
for v6 in range(v1):
    for v7 in range(v1):
        if v7 == v6:
            continue
        for v8 in range(v7 + 1, v1):
            if v8 == v6:
                continue
            v9 = v2[v7][v6][0] + v2[v6][v8][0]
            if v2[v7][v8][0] > v9:
                v5 = -1
            if v2[v7][v8][0] == v9:
                v2[v7][v8][1] = False
if v5 != -1:
    for v7 in range(v1):
        for v8 in range(v7 + 1, v1):
            if v2[v7][v8][1]:
                v5 += v2[v7][v8][0]
print(v5)
