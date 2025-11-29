v1, v2 = map(int, input().split())
v3 = [tuple(map(int, input().split())) for v4 in range(v2)]
v5 = [-float('inf')] * (v1 + 1)
v5[1] = 0
for v4 in range(v1):
    for v6, v7, v8 in v3:
        v5[v7] = max(v5[v7], v5[v6] + v8)
v9 = v5[v1]
for v4 in range(v1):
    for v6, v7, v8 in v3:
        v5[v7] = max(v5[v7], v5[v6] + v8)
if v9 < v5[v1]:
    print('inf')
else:
    print(v5[v1])
