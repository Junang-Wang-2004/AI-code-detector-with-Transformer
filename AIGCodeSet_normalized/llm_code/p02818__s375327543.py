v1, v2, v3 = map(int, input().split())
v4 = 0
while v4 < v3:
    if v1 > 0:
        v1 -= 1
        v4 += 1
    elif v2 > 0:
        v2 -= 1
        v4 += 1
print(v1, v2)
