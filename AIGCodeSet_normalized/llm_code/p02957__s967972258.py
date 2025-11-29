v1, v2 = map(int, input().split())
if (v1 + v2) % 2 == 0:
    print((v1 + v2) // 2)
else:
    print('IMPOSSIBLE')
