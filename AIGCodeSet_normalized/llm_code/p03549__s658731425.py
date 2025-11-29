v1, v2 = map(int, input())
v3 = (1900 * v2 + 100 * (v1 - v2)) * 2 ** v2
print(v3)
