v1, v2 = map(int, input().split())
v3 = [False for v4 in range(v1)]
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    for v4 in range(v5, v6 + 1):
        v3[v4] = True
v7 = []
for v4 in range(v1):
    if v3[v4]:
        v7.append(v4)
v8 = [0 for v4 in range(v1)]
v8[0] = 1
for v4 in range(1, v1):
    for v9 in v7:
        if v4 - v9 >= 0:
            v8[v4] += v8[v4 - v9]
print(v8[v1 - 1] % 998244353)
