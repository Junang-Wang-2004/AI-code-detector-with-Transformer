v1, v2, v3 = map(int, input().split())
v4 = v2 * (v1 - 1) + v3
v5 = v2 + v3 * (v1 - 1)
print(max(v5 - v4 + 1, 0))
