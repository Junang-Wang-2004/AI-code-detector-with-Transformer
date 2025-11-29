v1, v2, v3 = map(int, input().split())
v4 = abs(v1 - v2)
v5 = abs(v1 - v3)
if v4 < v5:
    print('A')
else:
    print('B')
