v1, v2 = map(int, input().split())
v3, v4 = map(int, input().split())
v5 = int(input())
if v2 == v4:
    v6 = v5 + 1
else:
    v6 = (v3 - v1) / (v2 - v4)
if v5 >= v6:
    if v6 > 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
