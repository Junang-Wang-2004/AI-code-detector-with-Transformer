v1, v2, v3 = tuple(map(int, input().split()))
if v2 + v3 <= v1:
    print('delicious')
elif v2 + v3 <= v1 + 1:
    print('safe')
else:
    print('dangerous')
