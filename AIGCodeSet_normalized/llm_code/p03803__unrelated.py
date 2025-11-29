v1, v2 = map(int, input().split())
if v1 == v2:
    print('Draw')
elif v1 == 1 or v2 == 1:
    print('Draw')
elif v1 > v2:
    print('Alice')
else:
    print('Bob')
