v1, v2, v3, v4 = map(int, input().split())
if v1 >= v4:
    print(v4)
else:
    v5 = v1
    v4 -= v1
    if v4 >= v2:
        v4 -= v2
    else:
        v5 -= v4
print(v5)
