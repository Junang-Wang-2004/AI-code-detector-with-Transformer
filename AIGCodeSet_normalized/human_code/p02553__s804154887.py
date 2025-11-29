v1, v2, v3, v4 = map(int, input().split())
print(max(max(v1 * v3, v1 * v4), max(v2 * v3, v2 * v4)))
