def f1(a1):
    v1 = len(a1)
    v2 = [0] * (v1 + 1)
    v3 = 0
    for v4 in range(v1):
        v2[v4 + 1] = v3 = (v3 * base + ord(a1[v4])) % mod
    return v2

def f2(a1):
    v1 = [1] * (a1 + 1)
    v2 = 1
    for v3 in range(a1):
        v1[v3 + 1] = v2 = v2 * base % mod
    return v1

def f3(a1, a2, a3, a4):
    return (a1[a4] - a1[a3] * a2[a4 - a3]) % mod

def f4(a1, a2, a3, a4, a5):
    for v1 in range(N - 2 * a1 + 1):
        v2 = f3(a2, a3, v1, a1 + v1)
        v3 = f3(a4, a5, v1, a1 + v1)
        for v4 in range(N - 2 * a1 - v1 + 1):
            if v2 == f3(a2, a3, v1 + a1 + v4, 2 * a1 + v1 + v4) and v3 == f3(a4, a5, v1 + a1 + v4, 2 * a1 + v1 + v4):
                return True
    return False
v1 = int(input())
v2 = input()
v3 = 1000000007
v4 = 37
v5 = f1(v2)
v6 = f2(v1)
v4 = 401
v7 = f1(v2)
v6 = f2(v1)
v8 = 1
v9 = v1 // 2
v10 = False
if v1 <= 26:
    v11 = set(list(v2))
    if v1 <= 3:
        if len(v11) < v1:
            print('1')
        else:
            print('0')
        v10 = True
    elif len(v11) == v1:
        print('0')
        v10 = True
while v10 == False:
    if v8 == v9:
        print(v8)
        v10 = True
    elif v9 - v8 == 1:
        if f4(v9, v5, b1, v7, v6):
            print(v9)
        else:
            print(v8)
        v10 = True
    else:
        v12 = (v8 + v9) // 2
        if f4(v12, v5, b1, v7, v6):
            v8 = v12
        else:
            v9 = v12 - 1
