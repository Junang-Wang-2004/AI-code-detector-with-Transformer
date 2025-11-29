v1, v2, v3 = map(int, input().split())
if v2 + v3 <= v1:
    print('delicious')
elif v3 <= v1 + v2:
    print('safe')
else:
    print('dangerous')
