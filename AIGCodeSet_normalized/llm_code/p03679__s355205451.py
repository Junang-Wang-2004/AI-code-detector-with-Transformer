v1, v2, v3 = list(map(int, input().split()))
if v2 - v3 >= 0:
    print('delicious')
elif abs(v2 - v3) < v1:
    print('safe')
else:
    print('dangerous')
