v1 = input().split()
v2 = [int(s) for v3 in v1]
v4 = v2[0]
v5 = v2[1]
v6 = v2[2]
v7 = v2[3]
for v8 in range(210):
    if v8 % 2 == 0:
        v6 -= v5
        if v6 <= 0:
            print('Yes')
            break
    else:
        v4 -= v7
        if v4 <= 0:
            print('No')
            break
