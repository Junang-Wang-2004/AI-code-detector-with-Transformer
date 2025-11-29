v1 = 1000000007
v2, v3 = map(int, input().split())
v4 = [0 for v5 in range(v3 + 1)]
for v5 in range(v3, 0, -1):
    v4[v5] = (v3 // v5) ** v2 % v1
    for v6 in range(2, v3 + 1):
        if v5 * v6 > v3:
            break
        else:
            v4[v5] = (v4[v5] - v4[v5 * v6] + v1) % v1
v7 = 0
for v5 in range(1, v3 + 1):
    v7 += v5 * v4[v5] % v1
print(v7 % v1)
