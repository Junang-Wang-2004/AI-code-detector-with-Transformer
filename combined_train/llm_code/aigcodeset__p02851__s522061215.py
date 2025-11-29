v1, v2 = [int(n) for v3 in input().split()]
v4 = [int(v3) for v3 in input().split()]
for v5 in range(v1 + 1, v2 + 1):
    if v2 % v5 == 0:
        v2 = v5
        break
v6 = 0
for v5 in range(1, v1 + 1):
    v4[v5 - 1] = (v4[v5 - 1] - 1) % v2
v7 = {0: [0]}
v8 = 0
for v5 in range(1, v1 + 1):
    v8 += v4[v5 - 1]
    if v8 >= v2:
        v8 -= v2
    if v8 in v7:
        v7[v8] = [j for v9 in v7[v8] if v5 - v9 < v2]
        v6 += len(v7[v8])
        v7[v8].append(v5)
    else:
        v7[v8] = [v5]
print(v6)
