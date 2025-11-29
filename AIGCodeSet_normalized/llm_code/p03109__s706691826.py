v1, v2, v3 = map(int, input().split('/'))
if 2019 <= v1 and (v2 <= 4 or (v2 == 5 and v3 <= 30)):
    print('Heisei')
else:
    print('TBD')
