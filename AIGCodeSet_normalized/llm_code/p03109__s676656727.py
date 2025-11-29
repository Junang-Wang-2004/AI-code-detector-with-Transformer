v1 = input()
if v1[:4] < '2019' or (v1[:4] == '2019' and v1[5:7] <= '04/30'):
    print('Heisei')
else:
    print('TBD')
