v1 = input()
v2 = len(v1) + 1
v3 = [0] * v2
v4 = [0] * v2
v4[0] = 1
for v5 in range(v2 - 1):
    v6 = int(v1[v5])
    v3[v5 + 1] = min(v3[v5] + v6, v4[v5] + 10 - v6)
    v6 += 1
    v4[v5 + 1] = min(v3[v5] + v6, v4[v5] + 10 - v6)
print(v3[-1])
