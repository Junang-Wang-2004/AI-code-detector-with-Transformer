v1 = list(map(int, input().split()))
if (v1[0] + v1[1]) // 2 == 0:
    print(abs(v1[0] - (v1[0] + v1[1]) // 2))
else:
    print('IMPOSSIBLE')
