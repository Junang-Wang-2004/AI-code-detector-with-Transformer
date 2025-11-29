v1 = int(input())
v2 = [list(map(float, input().split())) for v3 in range(v1)]
v4 = 0
for v5 in range(v1):
    for v6 in range(v1):
        if v5 == v6:
            pass
        else:
            v4 += ((v2[v5][0] - v2[v6][0]) ** 2 + (v2[v5][1] - v2[v6][1]) ** 2) ** (1 / 2)
v7 = 1
for v8 in range(1, v1 + 1):
    v7 *= v8
print(v4 / v1)
