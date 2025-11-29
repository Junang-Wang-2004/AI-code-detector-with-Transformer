v1, v2, v3 = map(int, input().split())
v4 = 10 ** 9 + 7
v5 = pow(2, v1) % v4

def f1(a1, a2):
    v1 = [0] * (a1 + 1)
    v1[0] = 1
    v1[1] = 1
    for v2 in range(2, a1 + 1):
        v1[v2] = v1[v2 - 1] * v2 % a2
    return v1

def f2(a1):
    v1 = f1(a1, 10 ** 9 + 7)
    v2 = v1[-1]
    v3 = 1
    v4 = [0] * (a1 + 1)
    v5 = [0] * 30
    v5[0] = v2
    v5[1] = v2 ** 2
    for v6 in range(28):
        v5[v6 + 2] = v5[v6 + 1] ** 2 % (10 ** 9 + 7)
    v7 = format(10 ** 9 + 5, 'b')
    for v8 in range(30):
        if v7[29 - v8] == '1':
            v3 = v3 * v5[v8] % (10 ** 9 + 7)
    v4[a1] = v3
    for v6 in range(a1, 0, -1):
        v4[v6 - 1] = v4[v6] * v6 % (10 ** 9 + 7)
    return v4
v6 = f2(2 * 10 ** 5 + 100)
if True:
    v7 = 1
    for v8 in range(v2):
        v7 *= v1 - v8
        v7 = v7 % v4
    v7 = v7 * v6[v2]
    v7 = v7 % v4
    v9 = 1
    for v8 in range(v3):
        v9 *= v1 - v8
        v9 = v9 % v4
    v9 = v9 % v4
    v9 = v9 * v6[v3]
    print((v5 - v7 - v9) % v4)
