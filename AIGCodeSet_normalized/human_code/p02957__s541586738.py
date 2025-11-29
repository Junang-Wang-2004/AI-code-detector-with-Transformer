v1, v2 = map(int, input().split())
v3 = sum([v1, v2]) // 2
if abs(v1 - v3) == abs(v2 - v3):
    print(v3)
else:
    print('IMPOSSIBLE')
