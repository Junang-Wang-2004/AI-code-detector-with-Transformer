v1, v2 = map(int, input().split())
v3 = []
v4 = v1 // 2
v5 = v1 // 2 + 1
for v6 in range(v2):
    if v1 % 2 == 0 and v5 - v4 + 2 * v6 >= v1 // 2:
        v3.append((v4 - v6 - 1, v5 + v6))
    else:
        v3.append((v4 - v6, v5 + v6))
for v7, v8 in sorted(v3):
    print(v7, v8)
