v1, v2 = list(map(int, input().split()))
v3 = [int(i) for v4 in input().split()]
v5 = {}
for v6, v7 in enumerate(v3, 1):
    v5[v6] = [v7, 'G']
for v8 in range(v2):
    v9, v10 = list(map(int, input().split()))
    if v5[v9][0] < v5[v10][0]:
        v5[v9][1] = 'N'
    elif v5[v10][0] < v5[v9][0]:
        v5[v10][1] = 'N'
v11 = v5.values()
v12 = 0
for v9 in v11:
    if v9[1] == 'G':
        v12 += 1
print(v12)
