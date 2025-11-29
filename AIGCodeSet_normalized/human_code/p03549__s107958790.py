v1, v2 = map(int, input().split())
v3 = 0
v3 += v2 * 1900
v3 += (v1 - v2) * 100
print(v3 * 2 ** v2)
