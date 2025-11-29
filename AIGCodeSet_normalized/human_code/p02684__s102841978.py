v1, v2 = map(int, input().split())
v3 = [0] + list(map(int, input().split()))
v4 = [float('INF') for v5 in range(v1 + 1)]
v6 = []
v7 = 0
v8 = 1
v9 = 0
while v7 == 0:
    if v4[v8] == float('INF'):
        v4[v8] = v9
        v6.append(v8)
        v8 = v3[v8]
        v9 += 1
    else:
        v7 = 1
        v10 = v4[v8]
        v11 = v9 - v10
if v2 < v10:
    print(v6[v2])
else:
    print(v6[(v2 - v10) % v11 + v10])
