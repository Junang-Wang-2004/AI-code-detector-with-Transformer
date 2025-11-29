v1, v2, v3, v4 = map(int, input().split())
if sorted([v1, v2, v3, v4]) == [1, 4, 7, 9]:
    print('YES')
else:
    print('NO')
