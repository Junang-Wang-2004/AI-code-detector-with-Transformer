v1, v2 = map(int, input().split())
v3 = min(v1, v2 // 2)
v4 = v2 - 2 * v3
v5 = v4 // 3
v6 = v3 + v5
print(v6)
