v1, v2, v3, v4, v5 = map(int, input().split())
v6, v7 = (60 * v1 + v2, 60 * v3 + v4)
print(abs(v6 - v7) - v5) if v7 - v5 > 0 else print(0)
