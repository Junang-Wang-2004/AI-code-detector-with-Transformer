v1 = 998244353
v2, v3 = map(int, input().split())
v4 = []
v5 = [0] * (v2 + 1)
v5[1] = 1
for v6 in range(v3):
    v7, v8 = map(int, input().split())
    v4.extend([x for v9 in range(v7, v8 + 1)])
v4.sort()
for v6 in range(2, v2 + 1):
    for v10 in v4:
        if v6 - v10 > 0:
            v5[v6] = (v5[v6] + v5[v6 - v10]) % v1
print(v5[v2])
