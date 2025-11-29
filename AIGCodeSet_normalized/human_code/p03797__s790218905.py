v1, v2 = map(int, input().split())
if v1 >= v2 // 2:
    v3 = v2 // 2
else:
    v3 = v1 + (v2 - 2 * v1) // 4
print(v3)
