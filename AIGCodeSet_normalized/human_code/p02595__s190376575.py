v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v5 = 0
for v6, v7 in v3:
    if v6 ** 2 + v7 ** 2 <= v2 ** 2:
        v5 += 1
print(v5)
