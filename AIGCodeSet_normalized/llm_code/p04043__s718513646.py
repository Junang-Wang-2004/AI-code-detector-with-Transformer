v1 = list(map(int, input().split()))
if (5 in v1 and 7 in v1) and (v1.count(5) >= 1 and v1.count(7) >= 1):
    print('YES')
else:
    print('NO')
