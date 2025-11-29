v1, v2, v3 = [int(x) for v4 in input().split('/')]
if v1 < 2019:
    print('Heisei')
elif v1 == 2019 and v2 <= 4:
    print('Heisei')
else:
    print('TBD')
