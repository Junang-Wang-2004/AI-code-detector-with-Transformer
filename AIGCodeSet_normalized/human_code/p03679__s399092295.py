v1, v2, v3 = list(map(int, input().split()))
if v3 - v2 <= 0:
    print('delicious')
elif v3 - v2 <= v1:
    print('safe')
else:
    print('dangerous')
