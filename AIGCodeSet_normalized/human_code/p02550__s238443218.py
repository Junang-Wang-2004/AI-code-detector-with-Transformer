v1, v2, v3 = map(int, input().split())
v4 = [0] * v3
v4[v2] = 1
v5 = -1
v6 = [v2]
for v7 in range(1, v1):
    v2 = v2 * v2 % v3
    if v4[v2] > 0:
        v5 = v2
        break
    v6.append(v2)
    v4[v2] += 1
if v5 < 0:
    print(sum(v6))
    exit()
v8 = v6.index(v5)
v9 = v6[:v8]
v10 = v6[v8:]
v11 = v1 - len(v9)
v12, v13 = divmod(v11, len(v10))
v14 = sum(v9) + sum(v10) * v12 + sum(v10[:v13])
print(v14)
