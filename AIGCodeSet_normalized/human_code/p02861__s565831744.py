v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append([int(x) for v4 in input().split()])
v5 = 0
for v6, v7 in v2:
    for v8, v9 in v2:
        v5 += ((v6 - v8) ** 2 + (v7 - v9) ** 2) ** 0.5
print(v5 / v1)
