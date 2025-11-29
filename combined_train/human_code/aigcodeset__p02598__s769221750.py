v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v3.sort()
for v4 in range(1, 31):
    if 2 ** v4 >= v3[-1] + 1:
        v5 = v4
        break
v6 = 2 ** (v5 - 1)
v7 = 2 ** (v5 - 1)
v8 = []
for v4 in range(v5 + 1):
    v9 = 0
    for v10 in range(v1):
        v9 += -(v3[v10] // -v6) - 1
    v7 = v7 // 2
    if v9 > v2:
        v6 = min(v3[-1], v6 + v7)
    else:
        v8.append(v6)
        v6 = max(1, v6 - v7)
print(min(v8))
