v1, v2, v3 = map(int, input().split())
v4 = int(input())
v5 = 0
for v6 in range(v1 + 1):
    for v7 in range(v2 + 1):
        for v8 in range(v3 + 1):
            v9 = 500 * v6 + 100 * v7 + 50 * v8
            if v9 == v4:
                v5 += 1
print(v5)
