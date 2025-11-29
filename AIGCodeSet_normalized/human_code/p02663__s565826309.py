v1, v2, v3, v4, v5 = map(int, input().split())
v6 = v3 * 60 + v4 - (v1 * 60 + v2)
print(v6 - v5)
