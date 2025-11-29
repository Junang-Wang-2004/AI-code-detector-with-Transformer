v1, v2 = list(map(int, input().split()))
v3 = (v1 + v2) / 2
if v3 == int(v3):
    print(int(v3))
else:
    print('IMPOSSIBLE')
