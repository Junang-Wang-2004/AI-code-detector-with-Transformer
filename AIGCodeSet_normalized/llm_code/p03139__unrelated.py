v1, v2, v3 = map(int, input().split())
v4 = min(v2, v3)
v5 = max(0, v2 + v3 - v1)
print(v4, v5)
