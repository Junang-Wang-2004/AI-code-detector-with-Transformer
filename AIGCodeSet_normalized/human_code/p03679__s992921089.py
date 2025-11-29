v1, v2, v3 = map(int, input().split())
if v2 >= v3:
    print('delicious')
elif v2 + v1 >= v3:
    print('safe')
else:
    print('dangerous')
