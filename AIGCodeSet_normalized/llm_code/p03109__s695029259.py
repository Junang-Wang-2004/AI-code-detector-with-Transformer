v1 = input().split('/')
if v1[0] >= 2020:
    print('TBD')
elif v1[0] == 2019:
    if v1[1] > 4:
        print('TBD')
    else:
        print('Heisei')
else:
    print('Heisei')
