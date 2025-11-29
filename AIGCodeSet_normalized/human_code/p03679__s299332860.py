v1, v2, v3 = map(int, input().split())
if v1 + v2 < v3:
    print('dangerous')
elif v2 >= v3:
    print('delicious')
else:
    print('safe')
