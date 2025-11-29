v1 = int(input())
if v1 % 2 == 1:
    print('0 0 0 1 1 ' + str(v1 // 2))
else:
    print('0 0 0 1 ' + str(v1 // 2) + ' ' + str(v1 // 2))
