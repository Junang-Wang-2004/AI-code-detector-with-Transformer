v1, v2, v3, v4 = map(int, input().split())
v5 = []
v5.append(v1 * v3)
v5.append(v2 * v3)
v5.append(v1 * v4)
v5.append(v2 * v4)
print(max(v5))
