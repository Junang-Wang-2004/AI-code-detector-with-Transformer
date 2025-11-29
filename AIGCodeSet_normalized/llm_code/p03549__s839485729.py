v1, v2 = map(int, input().split())
v3 = 100 * (v1 - v2) + 1900 * v2
v4 = 2 ** (-v2)
print(int(v3 / v4))
