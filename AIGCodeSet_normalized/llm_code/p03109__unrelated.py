from datetime import datetime
v1 = input()
v2 = datetime.strptime(v1, '%Y/%m/%d')
v3 = datetime(2019, 4, 30)
if v2 <= v3:
    print('Heisei')
else:
    print('TBD')
