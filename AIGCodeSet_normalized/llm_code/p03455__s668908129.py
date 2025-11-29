v1, v2 = map(int, input().split())
v3 = v1 * v2 % 2
if v3 == 0:
    print('Even')
else:
    print('Odd')
