v1, v2 = map(int, input().split())
v3 = [i for v4 in range(2, 14)] + [1]
v1 = v3.index(v1)
v2 = v3.index(v2)
if v1 > v2:
    print('Alice')
elif v2 > v1:
    print('Bob')
else:
    print('Draw')
