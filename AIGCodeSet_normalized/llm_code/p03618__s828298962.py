from sys import stdin
v1 = {}
v2 = stdin.readline().strip()
v3 = len(v2)
v1 = {}
for v4 in v2:
    v1[v4] = v1.get(v4, 0) + 1
v5 = v3 * (v3 + 1) // 2
v6 = 0
for v4 in range(v3 // 2):
    if v2[v4] != v2[v3 - 1 - v4]:
        v6 = 1
        break
v5 += v6
v7 = 0
for v8 in v1:
    v9 = v1[v8]
    v7 += v9 * (v9 + 1) // 2
print(v5 - v7)
