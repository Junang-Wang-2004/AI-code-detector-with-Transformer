v1, v2, v3, v4 = map(int, input().split())
print(min(v4, v1) * 1 + max(0, v4 - v1 - v2) * 0 + max(0, v4 - v1 - v2 - v3) * -1)
