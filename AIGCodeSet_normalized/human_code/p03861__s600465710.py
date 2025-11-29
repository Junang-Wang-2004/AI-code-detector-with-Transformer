v1, v2, v3 = map(int, input().split())
v4 = 0
if v1 == 0:
    v1 = 1
    v4 += 1
v4 += v2 // v3 - (v1 - 1) // v3
print(v4)
