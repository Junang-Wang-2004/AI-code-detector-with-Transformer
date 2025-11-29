v1, v2, v3 = map(int, input().split())
if v1 < v3 - v2:
    print('dangerous')
elif 0 < v3 - v2:
    print('safe')
else:
    print('delicious')
