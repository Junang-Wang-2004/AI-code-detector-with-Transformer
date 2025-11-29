v1, v2 = map(int, input().split())
v3 = 0
if v2 // 2 >= v1:
    v3 += v1
    v2 = v2 - v1 * 2
    v3 += v2 // 4
else:
    v3 += v2 // 2
print(v3)
