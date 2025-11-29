v1, v2, v3 = map(int, input().split())
if v1 >= v3:
    v1 -= v3
else:
    v3 -= v1
    v1 = 0
    if v2 >= v3:
        v2 -= v3
    else:
        v2 = 0
print(str(v1) + ' ' + str(v2))
