v1 = [[0 for v2 in range(10)] for v3 in range(10)]
v4, v5 = map(int, input().split())
for v3 in range(10):
    v6 = list(map(int, input().split()))
    for v2 in range(10):
        v1[v3][v2] = v6[v2]
for v7 in range(10):
    for v3 in range(10):
        for v2 in range(10):
            v1[v3][v2] = min(v1[v3][v2], v1[v3][v7] + v1[v7][v2])
v8 = 0
for v3 in range(v4):
    v6 = list(map(int, input().split()))
    for v2 in range(v5):
        if v6[v2] == -1 or v6[v2] == 1:
            continue
        else:
            v8 += v1[v6[v2]][1]
print(v8)
