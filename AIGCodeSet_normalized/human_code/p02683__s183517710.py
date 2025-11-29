v1, v2, v3 = map(int, input().split())
v4 = []
v5 = []
for v6 in range(v1):
    v7 = list(map(int, input().split()))
    v4.append(v7[0])
    v5.append(v7[1:])
v8 = float('inf')
for v9 in range(2 ** v1):
    v10 = [0] * v2
    v11 = 0
    for v12 in range(v1):
        if v9 >> v12 & 1:
            v11 += v4[v12]
            for v13 in range(v2):
                v10[v13] += v5[v12][v13]
    if all([v10[l] >= v3 for v14 in range(v2)]):
        v8 = min(v8, v11)
if v8 != float('inf'):
    print(v8)
else:
    print('-1')
