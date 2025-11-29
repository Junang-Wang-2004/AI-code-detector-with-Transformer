def f1(a1):
    for v1 in range(g):
        now[v1] += c[v1][a1]
    for v1 in range(g):
        if now[v1] > k:
            return False
    return True
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)
v1 = float('inf')
v2 = [[0] * 10 for v3 in range(1005)]
v4, v5, v6 = map(int, input().split())
v7 = [[int(i) for v8 in input()] for v3 in range(v4)]
v9 = v1
for v10 in range(1 << v4 - 1):
    v11 = 0
    id = [0] * v4
    for v8 in range(v4):
        id[v8] = v11
        if v10 >> v8 & 1:
            v11 += 1
    v11 += 1
    for v8 in range(v11):
        for v12 in range(v5):
            v2[v8][v12] = 0
    for v8 in range(v4):
        for v12 in range(v5):
            v2[id[v8]][v12] += v7[v8][v12]
    v13 = True
    for v8 in range(v11):
        for v12 in range(v5):
            if v2[v8][v12] > v6:
                v13 = False
                break
        if not v13:
            break
    if not v13:
        continue
    v14 = v11 - 1
    v15 = [0] * v11
    for v12 in range(v5):
        if not f1(v12):
            v14 += 1
            v15 = [0] * v11
            f1(v12)
    v9 = min(v9, v14)
print(v9)
