v1 = int(input())
v2 = [tuple(map(int, input().split())) for v3 in range(v1)]
v4, v5 = (1, 1)
for v6, v7 in v2:
    if v6 < v4 or v7 < v5:
        v8 = max((v4 - 1) // v6 + 1, (v5 - 1) // v7 + 1)
        v6 *= v8
        v7 *= v8
    v4, v5 = (v6, v7)
print(v4 + v5)
