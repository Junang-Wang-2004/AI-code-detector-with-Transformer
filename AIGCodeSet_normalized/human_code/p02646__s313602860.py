v1, v2 = map(int, input().split())
v3, v4 = map(int, input().split())
v5 = int(input())
v6 = v2 - v4
v7 = abs(v1 - v3)
if v6 * v5 >= v7:
    print('YES')
else:
    print('NO')
