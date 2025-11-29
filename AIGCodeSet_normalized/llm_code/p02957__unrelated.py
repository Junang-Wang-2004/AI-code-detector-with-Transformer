v1, v2 = map(int, input().split())
v3 = (v1 + v2) // 2
if v1 < v3 < v2:
    print('IMPOSSIBLE')
else:
    print(v3)
