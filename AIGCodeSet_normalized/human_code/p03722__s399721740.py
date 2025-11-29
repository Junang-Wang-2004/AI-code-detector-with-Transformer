v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v5 = [-float('inf')] * (v1 + 1)
v5[1] = 0
for v4 in range(v1 - 1):
    for v6 in v3:
        v7, v8, v9 = v6
        v5[v8] = max(v5[v8], v5[v7] + v9)
v10 = v5[v1]
for v4 in range(v1):
    for v6 in v3:
        v7, v8, v9 = v6
        v5[v8] = max(v5[v8], v5[v7] + v9)
if v5[v1] == v10:
    print(v10)
else:
    print('inf')
