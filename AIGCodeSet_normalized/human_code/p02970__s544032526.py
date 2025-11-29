v1, v2 = map(int, input().split())
v3 = 2 * v2 + 1
if v1 % v3 == 0:
    v4 = v1 / v3
else:
    v4 = (v1 - v1 % v3) / v3 + 1
print(int(v4))
