v1, v2 = map(int, input().split())
v3 = []
v4 = 0
for v5 in range(1, 1000):
    v4 += v5
    v3.append(v4)
v6 = v1 - v2
print(v3[v6] - v2)
