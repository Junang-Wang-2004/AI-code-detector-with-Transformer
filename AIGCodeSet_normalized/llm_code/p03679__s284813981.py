v1, v2, v3 = (int(i) for v4 in input().split())
v5 = v3 - v2
if v5 <= 0:
    print('delicious')
elif v5 <= v1:
    print('safe')
else:
    print('dangerous')
