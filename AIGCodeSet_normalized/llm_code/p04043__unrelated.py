v1, v2, v3 = map(int, input().split())
if v1 == 5 and v2 == 7 and (v3 == 5) or (v1 == 7 and v2 == 5 and (v3 == 5)) or (v1 == 5 and v2 == 5 and (v3 == 7)):
    print('YES')
else:
    print('NO')
