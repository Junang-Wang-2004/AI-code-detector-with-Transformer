v1 = int(input())
v2 = int((2 * v1) ** 0.5)
if v2 * (v2 + 1) // 2 < v1:
    v2 += 1
v3 = v1 - v2 * (v2 - 1) // 2
if v3 <= v2:
    print(v2)
else:
    print(v2 + 1)
