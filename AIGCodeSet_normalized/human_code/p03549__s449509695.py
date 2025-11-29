v1, v2 = map(int, input().split())
v3 = (1900 * v2 + (v1 - v2) * 100) * 2 ** v2
print(v3)
