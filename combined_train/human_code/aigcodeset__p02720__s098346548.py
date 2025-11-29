if True:
    v1 = int(input())
else:
    v1 = 100000
v2 = 0
v3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
v2 = len(v3)
if v2 >= v1:
    print(v3[v1 - 1])
    exit()
while v2 < v1:
    v4 = []
    v5 = len(str(v3[0]))
    for v6 in v3:
        v7 = str(v6)
        v8 = int(v7[len(v7) - 1])
        if v8 == 0:
            v4.append(v6 * 10 + v8)
            v4.append(v6 * 10 + 1)
        elif v8 == 9:
            v4.append(v6 * 10 + 8)
            v4.append(v6 * 10 + v8)
        else:
            v4.append(v6 * 10 + v8 - 1)
            v4.append(v6 * 10 + v8)
            v4.append(v6 * 10 + v8 + 1)
    if v2 + len(v4) < v1:
        v3 = v4
        v2 += len(v3)
    else:
        print(v4[v1 - v2 - 1])
        break
