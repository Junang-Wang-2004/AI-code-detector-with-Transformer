v1, v2, v3 = map(int, input().split())
v4 = v1 + v2
if v3 == v4:
    print('0 0')
elif v4 < v3:
    print('0', v3 - v4)
else:
    print(v1 - v3, v2)
