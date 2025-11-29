def f1(a1):
    v1 = []
    v2 = a1
    for v3 in range(2, int(-(-a1 ** 0.5 // 1)) + 1):
        if v2 % v3 == 0:
            v4 = 0
            while v2 % v3 == 0:
                v4 += 1
                v2 //= v3
            v1.append([v3, v4])
    if v2 != 1:
        v1.append([v2, 1])
    if v1 == []:
        v1.append([a1, 1])
    return v1
v1 = 10 ** 9 + 7
v2 = 200000
v3 = [-1 for v4 in range(v2 + 1)]
v5 = [-1 for v4 in range(v2 + 1)]
v6 = [-1 for v4 in range(v2 + 1)]

def f2(a1=v2):
    v3[0] = 0
    for v1 in range(1, a1):
        v3[v1] = f3(v1)

def f3(a1, a2=v1):
    v1, v2, v3, v4 = (a2, 1, 0, a1)
    while v1:
        v5 = v4 // v1
        v4 -= v5 * v1
        v4, v1 = (v1, v4)
        v2 -= v5 * v3
        v2, v3 = (v3, v2)
    v2 %= a2
    if v2 < 0:
        v2 += a2
    return v2

def f4(a1, a2, a3=v1):
    v1 = 1
    while a2:
        if a2 & 1:
            v1 = v1 * a1 % a3
        a1 = a1 * a1 % a3
        a2 >>= 1
    return v1

def f5(a1=v2, a2=v1):
    v1 = 1
    v5[0] = v6[0] = 1
    for v2 in range(1, a1):
        v1 *= v2
        v1 %= a2
        v5[v2] = v1
        v6[v2] = f3(v1, a2)

def f6(a1, a2, a3=v1):
    if v5[0] == -1:
        f5()
    return v5[a1] * v6[a2] * v6[a1 - a2] % a3
v7, v8 = [int(_) for v9 in input().split()]
v10 = 1
for v11, v12 in f1(v8):
    v10 *= f6(v7 - 1 + v12, v12)
    v10 %= v1
print(v10)
