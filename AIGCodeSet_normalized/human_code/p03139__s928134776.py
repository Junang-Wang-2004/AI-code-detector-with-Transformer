v1, v2, v3 = [int(_) for v4 in input().split()]
v5 = v2 + v3 - v1
if v5 < 0:
    v5 = 0
print(min(v2, v3), v5)
