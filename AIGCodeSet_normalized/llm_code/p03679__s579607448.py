v1, v2, v3 = map(int, input().split())
v4 = v2 - v3
if v4 > 0:
    print('delicious')
elif abs(v4) > v1:
    print('dangerous')
else:
    print('safe')
