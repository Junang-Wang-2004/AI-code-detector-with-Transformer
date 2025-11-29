v1 = int(input())
v2 = []
for v3 in range(v1):
    v4, v5 = map(int, input().split())
    v2.append((v4, v5))
v6 = v2[0][0] + v2[0][1]
for v7 in range(1, v1):
    v4, v5 = v2[v7]
    v8 = 1
    for v9 in range(2, min(v4, v5) + 1):
        if v4 % v9 == 0 and v5 % v9 == 0:
            v8 = v9
    v6 = max(v6, v2[v7 - 1][0] * v5 // v8 + v2[v7 - 1][1] * v4 // v8)
print(v6)
