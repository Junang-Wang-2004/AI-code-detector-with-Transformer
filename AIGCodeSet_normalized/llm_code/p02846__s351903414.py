v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = v2[0] * v1[0]
v5 = v3[0] * v1[0]
v6 = v4 + v2[1] * v1[1]
v7 = v5 + v3[1] * v1[1]
v8 = v4 - v5
v9 = v6 - v7
if v8 * v9 > 0:
    print(0)
elif v8 * v9 == 0:
    print('infinity')
elif v8 > 0:
    print(1 + 2 * (abs(v9) // v8))
else:
    print(1 + 2 * (abs(v8) // v9))
