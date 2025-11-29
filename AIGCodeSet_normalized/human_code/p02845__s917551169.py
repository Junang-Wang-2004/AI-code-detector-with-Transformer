v1 = 10 ** 9 + 7
v2 = int(input())
v3 = list(map(int, input().split()))
v4 = 0
v5 = 0
v6 = 0
v7 = -1
v8 = 1
for v9, v10 in enumerate(v3):
    if v9 == 0:
        if v10 != 0:
            v7 = 0
            break
        else:
            v4 = 1
            v8 *= 3
    elif v4 == v10 and v5 == v10 and (v6 == v10):
        v8 *= 3
        v4 += 1
    elif v4 == v10 and v5 == v10:
        v8 *= 2
        v4 += 1
    elif v4 == v10 and v6 == v10:
        v8 *= 2
        v4 += 1
    elif v5 == v10 and v6 == v10:
        v8 *= 2
        v5 += 1
    elif v4 == v10:
        v4 += 1
    elif v5 == v10:
        v5 += 1
    elif v6 == v10:
        v6 += 1
    else:
        v7 = 0
        break
if v7 == 0:
    print(v7)
else:
    v7 = v8
    print(v7 % v1)
