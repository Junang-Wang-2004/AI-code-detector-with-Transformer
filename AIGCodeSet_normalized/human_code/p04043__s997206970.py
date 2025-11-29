v1 = list(map(int, input().split()))
v1.sort()
v2 = 0
if v1[0] == 5:
    if v1[1] == 5:
        if v1[2] == 7:
            print('YES')
            v2 += 1
if v2 == 0:
    print('NO')
