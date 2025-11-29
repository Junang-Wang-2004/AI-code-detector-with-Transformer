v1, v2, v3 = map(int, input().split())
print(min(v2, v3), max(v2 + v3 - v1, 0))
