v1, v2 = map(int, input().split())
if v1 == 1:
    v1 = 14
if v2 == 1:
    v2 = 14
if v1 < v2:
    print('Bob')
elif v1 > v2:
    print('Alice')
else:
    print('Draw')
