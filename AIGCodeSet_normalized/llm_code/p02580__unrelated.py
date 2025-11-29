v1, v2, v3 = map(int, input().split())
v4 = set()
for v5 in range(v3):
    v6, v7 = map(int, input().split())
    v4.add((v6, v7))
v8 = 0
for v6 in range(1, v1 + 1):
    for v7 in range(1, v2 + 1):
        v9 = 0
        for v10, v11 in v4:
            if v10 == v6 or v11 == v7:
                v9 += 1
        v8 = max(v8, v9)
print(v8)
