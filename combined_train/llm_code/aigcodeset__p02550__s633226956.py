v1 = x
v2 = v1
v3 = [0] * m
v4 = [v1]
v5 = 0
for v6 in range(1, m + 1):
    if n <= v6:
        break
    v7 = v1 * v1 % m
    v1 = v7
    if v3[v1] == 1:
        v5 = v4.index(v1)
        break
    else:
        v2 += v7
        v4.append(v1)
        v3[v1] = 1
if v5 != 0:
    v8 = v4[v5:]
    v7 = sum(v8)
    v9 = (n - len(v4)) // len(v8)
    v10 = n - len(v4) - v9 * len(v8)
    v2 = v2 + v9 * v7 + sum(v8[:v10])
print(v2)
