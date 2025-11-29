v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v1):
    v6 = list(map(int, input().split()))
    v4.append(v6)
v7 = float('inf')
for v5 in range(2 ** v1):
    v8 = [0] * v2
    v9 = 0
    for v10 in range(v1):
        if v5 >> v10 & 1:
            for v11 in range(v2):
                v8[v11] += v4[v10][v11 + 1]
            v9 += v4[v10][0]
    if all((l >= v3 for v12 in v8)):
        v7 = min(v7, v9)
if v7 == float('inf'):
    print('-1')
else:
    print(v7)
