v1, v2 = map(int, input().split())
v3 = v1 * v2
if v3 % 2 == 0:
    print('Even')
elif v3 % 2 == 1:
    print('Odd')
