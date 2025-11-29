v1, v2, v3 = map(int, input().split())
v4 = [[0] * v2 for v5 in range(v1)]
v6 = [0] * v1
v7 = 10 ** 10
for v8 in range(v1):
    v9 = list(map(int, input().split()))
    v6[v8] = v9[0]
    v4[v8] = v9[1:]
import itertools
for v10 in itertools.product([0, 1], repeat=v1):
    v9 = [0] * v2
    v11 = 0
    for v8 in range(v1):
        if v10[v8] == 1:
            for v12 in range(len(v4[v8])):
                v9[v12] += v4[v8][v12]
            v11 += v6[v8]
    v13 = False
    for v8 in range(len(v9)):
        if v9[v8] < v3:
            v13 = True
    if v13:
        pass
    else:
        v7 = min(v7, v11)
if v7 != 10 ** 10:
    print(v7)
else:
    print(-1)
