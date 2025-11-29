v1 = 10 ** 9 + 7
v2, v3 = map(int, input().split())
v4 = [[] for v5 in range(v2)]
for v5 in range(v2 - 1):
    v6, v7 = map(int, input().split())
    v4[v6 - 1] += [v7 - 1]
    v4[v7 - 1] += [v6 - 1]
v8 = [0] * v2
v9 = [0]
v8[0] = 1
v10 = v3
while v9:
    v11 = v9.pop()
    for v12 in v4[v11]:
        if v8[v12] > 0:
            continue
        else:
            v10 = v10 * max(v3 - v8[v11], 0) % v1
            v8[v11] += 1
            v8[v12] = 2
            v9.append(v12)
print(v10 % v1)
