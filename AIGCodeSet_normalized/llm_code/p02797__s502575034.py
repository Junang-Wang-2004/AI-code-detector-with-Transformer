v1, v2, v3 = map(int, input().split())
v4 = [v3] * v2 + [v3 + 1] * (v1 - v2)
print(*v4)
