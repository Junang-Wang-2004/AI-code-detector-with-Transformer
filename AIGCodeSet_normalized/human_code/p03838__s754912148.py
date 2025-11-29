v1, v2 = map(int, input().split())
v3 = abs(v2) - abs(v1)
if v3 == 0:
    v4 = 1
elif v3 > 0:
    if v1 >= 0 and v2 >= 0:
        v4 = v3
    elif v1 < 0 and v2 < 0:
        v4 = v3 + 2
    else:
        v4 = v3 + 1
elif v3 < 0:
    if v1 > 0 and v2 > 0:
        v4 = -v3 + 2
    elif v1 <= 0 and v2 <= 0:
        v4 = -v3
    else:
        v4 = -v3 + 1
print(v4)
