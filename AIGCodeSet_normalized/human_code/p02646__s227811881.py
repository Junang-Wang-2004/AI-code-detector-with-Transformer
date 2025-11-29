v1, v2 = map(int, input().split())
v3, v4 = map(int, input().split())
v5 = int(input())
v6 = v1 + v2 * v5
v7 = v3 + v4 * v5
v8 = v1 - v2 * v5
v9 = v3 - v4 * v5
if v1 <= v3:
    if v6 >= v7:
        print('YES')
    else:
        print('NO')
elif v8 <= v9:
    print('YES')
else:
    print('NO')
