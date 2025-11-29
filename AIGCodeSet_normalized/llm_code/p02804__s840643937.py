import sys
v1 = sys.stdin.readline
v2 = pow(10, 9) + 7

def f1(a1, a2):
    global fac, finv
    if a1 < a2:
        return 0
    if a1 < 0 or a2 < 0:
        return 0
    return fac[a1] * (finv[a2] * finv[a1 - a2] % v2) % v2

def f2():
    global fac, finv
    v1, v2 = map(int, v1().split())
    v3 = list(map(int, v1().split()))
    v3.sort()
    v4 = v1 + 1
    v5 = [0 for v6 in range(v4)]
    v7 = [0 for v6 in range(v4)]
    v8 = [0 for v6 in range(v4)]
    v5[0] = v5[1] = 1
    v7[0] = v7[1] = 1
    v8[1] = 1
    for v9 in range(2, v4):
        v5[v9] = v5[v9 - 1] * v9 % v2
        v8[v9] = v2 - v8[v2 % v9] * (v2 // v9) % v2
        v7[v9] = v7[v9 - 1] * v8[v9] % v2
    v10 = 0
    v11 = 0
    for v9 in range(v2):
        v10 += v3[v1 - v9 - 1] * f1(v1 - v9 - 1, v2 - 1)
        v11 += v3[v9] * f1(v9, v2 - 1)
    v12 = (v10 - v11) % v2
    print(v12)
if __name__ == '__main__':
    f2()
