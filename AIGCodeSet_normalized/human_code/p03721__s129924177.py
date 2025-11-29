v1, v2 = map(int, input().split())
v3 = [[int(_) for v4 in input().split()] for v4 in range(v1)]
v3 = sorted(v3, key=lambda x: x[0])
v5 = 0
for v6 in v3:
    v5 += v6[1]
    if v5 >= v2:
        v7 = v6[0]
        break
print(v7)
