v1 = int(input())
v2 = int(input())
v3 = int(input())
if v2 <= v1 and v3 <= v1:
    print('delicious')
elif v2 > v1 and v3 <= v1:
    print('safe')
else:
    print('dangerous')
