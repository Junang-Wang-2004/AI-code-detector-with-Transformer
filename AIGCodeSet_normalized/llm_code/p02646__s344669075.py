v1, v2 = map(int, input().split())
v3, v4 = map(int, input().split())
v5 = int(input())
v6 = 0
v7 = 0
if v4 >= v2:
    print('NO')
else:
    v6 = v2 * v5
    v7 = v4 * v5
    v8 = abs(v1 - v3)
    if v7 + v8 <= v6:
        print('YES')
    else:
        print('NO')
