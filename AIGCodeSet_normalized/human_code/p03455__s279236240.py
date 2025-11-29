v1 = list(map(int, input().strip().split(' ')))
v2 = v1[0]
v3 = v1[1]
if v2 % 2 == 0 or v3 % 2 == 0:
    print('Even')
else:
    print('Odd')
