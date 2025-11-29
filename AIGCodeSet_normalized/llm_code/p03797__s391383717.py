v1, v2 = map(int, input().split())
v3 = v1 % (v2 // 2)
v4 = v2 - 2 * v3
v3 += v4 // 4
print(v3)
