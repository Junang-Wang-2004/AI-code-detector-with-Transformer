v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = []
for v6 in range(v1 - 1):
    v5.append(v4[v6 + 1] - v4[v6])
v7 = 0
for v6 in range(len(v5)):
    if v5[v6] * v2 < v3:
        v7 += v5[v6] * v2
    else:
        v7 += v3
print(v7)
