v1, v2 = map(int, input().split())
v3 = []
v3.append([0 for v4 in range(v2 + 1)])
for v4 in range(v2):
    v5 = [0] + list(map(int, input().split()))
    v3.append(v5)
v6 = []
for v4 in range(v1):
    v7 = list(map(int, input().split()))
    v6.append(v7)
v8 = [0 for v4 in range(v2 + 1)]
v9 = [0 for v4 in range(v2 + 1)]
v10 = [0 for v4 in range(v2 + 1)]
for v4 in range(v1):
    for v11 in range(v1):
        if (v4 + v11) % 3 == 0:
            v8[v6[v4][v11]] += 1
        elif (v4 + v11) % 3 == 1:
            v9[v6[v4][v11]] += 1
        elif (v4 + v11) % 3 == 2:
            v10[v6[v4][v11]] += 1
v12 = [v4 for v4 in range(1, v2 + 1)]
import itertools
v13 = list(itertools.permutations(v12, 3))
v14 = 10 ** 20
for v4 in range(len(v13)):
    v15 = 0
    for v11 in range(1, v2 + 1):
        v15 += v8[v11] * v3[v11][v13[v4][0]]
        v15 += v9[v11] * v3[v11][v13[v4][1]]
        v15 += v10[v11] * v3[v11][v13[v4][2]]
    if v14 > v15:
        v14 = v15
print(v14)
