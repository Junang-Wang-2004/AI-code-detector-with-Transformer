import math

def f1(a1, a2):
    v1 = math.gcd(a1, a2)
    return (a1 // v1, a2 // v1)

def f2(a1, a2, a3=10 ** 9 + 7):
    """
    O(log n)
    """
    if a2 == 0:
        return 1
    if a2 % 2 == 0:
        return f2(a1 ** 2 % 1000000007, a2 // 2) % a3
    else:
        return a1 * f2(a1 ** 2 % 1000000007, (a2 - 1) // 2) % a3 % a3

def f3():
    v1 = int(input())
    v2 = dict()
    v3 = dict()
    v4 = [0, 0]
    v5 = 0
    for v6 in range(v1):
        v7, v8 = map(int, input().split())
        if v7 == 0 and v8 == 0:
            v5 += 1
            continue
        if v7 == 0:
            v8 = -abs(v8)
        if v8 == 0:
            v7 = abs(v7)
        if v7 < 0:
            v7 *= -1
            v8 *= -1
        v9 = f1(v7, v8)
        if v8 < 0:
            if not v9 in v2:
                v2[v9] = 0
            v2[v9] += 1
        else:
            if not v9 in v3:
                v3[v9] = 0
            v3[v9] += 1
    v10 = 1
    v11 = []
    for (v12, v13), v14 in v2.items():
        if (-v13, v12) in v3:
            v11.append((v14, v3[-v13, v12]))
            del v3[-v13, v12]
        else:
            v11.append((v14, 0))
    for v14 in v3.values():
        v11.append((v14, 0))
    for v6, v15 in v11:
        v10 *= (f2(2, v6) + f2(2, v15) - 1) % 1000000007
        v10 %= 1000000007
    print((v10 + v5 - 1) % (10 ** 9 + 7))
f3()
