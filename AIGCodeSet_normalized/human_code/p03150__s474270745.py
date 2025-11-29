v1 = input()
if v1[0:7] == 'keyence':
    print('YES')
elif v1[-7:] == 'keyence':
    print('YES')
elif v1[0:1] == 'k' and v1[-6:] == 'eyence':
    print('YES')
elif v1[0:2] == 'ke' and v1[-5:] == 'yence':
    print('YES')
elif v1[0:3] == 'key' and v1[-4:] == 'ence':
    print('YES')
elif v1[0:4] == 'keye' and v1[-3:] == 'nce':
    print('YES')
elif v1[0:5] == 'keyen' and v1[-2:] == 'ce':
    print('YES')
elif v1[0:6] == 'keyenc' and v1[-1:] == 'e':
    print('YES')
else:
    print('NO')
