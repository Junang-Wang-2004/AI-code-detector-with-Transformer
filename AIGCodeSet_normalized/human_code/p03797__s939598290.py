v1, v2 = (int(i) for v3 in input().split())
if v2 <= 2 * v1:
    v4 = (v2 - v2 % 2) // 2
else:
    v4 = v1
    v5 = v2 - 2 * v1
    v4 += (v5 - v5 % 4) // 4
print(v4)
