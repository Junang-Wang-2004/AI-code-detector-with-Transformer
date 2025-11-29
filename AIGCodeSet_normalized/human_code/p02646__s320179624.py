v1, v2 = map(int, input().split())
v3, v4 = map(int, input().split())
v5 = int(input())
v6 = abs(v1 - v3)
v7 = v2 - v4
if v7 <= 0:
    print('NO')
elif v7 > 0:
    if v7 * v5 >= v6:
        print('YES')
    else:
        print('NO')
