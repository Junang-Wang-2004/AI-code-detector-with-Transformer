v1, v2, v3 = map(int, input().split())
if v1 >= v3:
    print(str(v1 - v3) + ' ' + str(v2))
elif v1 + v2 >= v3:
    print('0 ' + str(v2 - (v3 - v1)))
else:
    print('0 0')
