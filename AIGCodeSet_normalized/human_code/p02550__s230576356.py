v1, v2, v3 = map(int, input().split())
v4 = [v2]
v5 = [-1] * (v3 + 1)
v5[v2] = 0
v6 = 0
for v7 in range(v1 - 1):
    v6 = v4[-1] ** 2 % v3
    if v5[v6] >= 0:
        break
    v4.append(v6)
    v5[v6] = v7 + 1
v6 = v5[v6]
v8 = len(v4) - v6
print(sum(v4[:v6]) + (v1 - v6) // v8 * sum(v4[v6:]) + sum(v4[v6:v6 + (v1 - v6) % v8]))
