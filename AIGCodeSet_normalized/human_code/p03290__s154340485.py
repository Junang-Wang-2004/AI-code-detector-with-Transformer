v1, v2 = map(int, input().split())
v3, v4 = ([], [])
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v3.append(v6)
    v4.append(v7)
v8 = float('inf')
for v9 in range(1 << v1):
    v10 = [v5 for v5 in range(v1)]
    v11 = 0
    v12 = 0
    for v5 in range(v1):
        if v9 & 1 << v5:
            v11 += v3[v5]
            v12 += (v5 + 1) * 100 * v3[v5] + v4[v5]
            v10.remove(v5)
    if v12 < v2:
        for v5 in v10[::-1]:
            for v13 in range(v3[v5]):
                v11 += 1
                v12 += (v5 + 1) * 100
                if v12 >= v2:
                    break
            else:
                continue
            break
    if v11 <= v8:
        v8 = v11
print(v8)
