v1, v2 = map(int, input().split())
v3 = 100 * (v1 - v2) + 1900 * v2
v4 = (1 / 2) ** v2
print(v3 * v4 / (1 - v4) ** 2)
