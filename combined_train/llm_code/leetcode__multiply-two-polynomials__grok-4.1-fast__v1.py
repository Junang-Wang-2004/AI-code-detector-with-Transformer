import math
import cmath

def f1(a1, a2):
    v1 = len(a1)
    if v1 <= 1:
        return
    v2 = (v1 - 1).bit_length()
    for v3 in range(v1):
        v4 = 0
        v5 = v3
        for v6 in range(v2):
            v4 = v4 << 1 | v5 & 1
            v5 >>= 1
        if v3 < v4:
            a1[v3], a1[v4] = (a1[v4], a1[v3])
    v7 = 2
    while v7 <= v1:
        v8 = 2 * math.pi / v7 * (-1 if a2 else 1)
        v9 = complex(math.cos(v8), math.sin(v8))
        for v10 in range(0, v1, v7):
            v11 = complex(1, 0)
            v12 = v7 // 2
            for v13 in range(v12):
                v14 = v10 + v13
                v15 = v14 + v12
                v16 = a1[v14]
                v17 = a1[v15] * v11
                a1[v14] = v16 + v17
                a1[v15] = v16 - v17
                v11 *= v9
        v7 *= 2
    if a2:
        v18 = 1.0 / v1
        for v19 in range(v1):
            a1[v19] *= v18

def f2(a1, a2):
    v1 = len(a1) + len(a2) - 1
    v2 = 1
    while v2 < v1:
        v2 <<= 1
    v3 = [complex(coef, 0) for v4 in a1] + [0j] * (v2 - len(a1))
    v5 = [complex(v4, 0) for v4 in a2] + [0j] * (v2 - len(a2))
    f1(v3, False)
    f1(v5, False)
    for v6 in range(v2):
        v3[v6] *= v5[v6]
    f1(v3, True)
    return [int(round(c.real)) for v7 in v3[:v1]]

class C1(object):

    def multiply(self, a1, a2):
        return f2(a1, a2)
