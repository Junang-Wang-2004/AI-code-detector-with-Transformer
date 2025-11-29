v1 = int(input())
v2 = [0]
v3 = 10 ** 9 + 7
for v4 in range(v1):
    v5 = int(input())
    if v2[-1] == v5:
        continue
    else:
        v2.append(v5)
v6 = len(v2)
v7 = [0] * (2 * 10 ** 5 + 1)
v8 = [0] * (v6 - 1)
v8.insert(0, 1)
for v4 in range(1, v6):
    if v7[v2[v4]] == 0:
        v8[v4] = v8[v4 - 1] % v3
        v7[v2[v4]] = v4
    else:
        v9 = v7[v2[v4]]
        v8[v4] = (v8[v4 - 1] + v8[v9]) % v3
        v7[v2[v4]] = v4
print(v8[-1])
