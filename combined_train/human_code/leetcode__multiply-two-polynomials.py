import math
import cmath

def f1(a1, a2):
    v1 = len(a1)
    if v1 <= 1:
        return
    v2 = 0
    for v3 in range(1, v1):
        v4 = v1 >> 1
        while v2 & v4:
            v2 ^= v4
            v4 >>= 1
        v2 ^= v4
        if v3 < v2:
            a1[v3], a1[v2] = (a1[v2], a1[v3])
    v5 = 2
    while v5 <= v1:
        v6 = 2 * math.pi / v5 * (-1 if a2 else 1)
        v7 = complex(math.cos(v6), math.sin(v6))
        for v3 in range(0, v1, v5):
            v8 = complex(1)
            for v2 in range(v5 // 2):
                v9 = a1[v3 + v2]
                v10 = a1[v3 + v2 + v5 // 2] * v8
                a1[v3 + v2] = v9 + v10
                a1[v3 + v2 + v5 // 2] = v9 - v10
                v8 *= v7
        v5 <<= 1
    if a2:
        for v3 in range(v1):
            a1[v3] /= v1

def f2(a1, a2):
    v1, v2 = (len(a1), len(a2))
    v3, v4 = (1, v1 + v2 - 1)
    while v3 < v4:
        v3 <<= 1
    a1 = [complex(x, 0) for v6 in a1] + [0] * (v3 - v1)
    a2 = [complex(v6, 0) for v6 in a2] + [0] * (v3 - v2)
    f1(a1, invert=False)
    f1(a2, invert=False)
    for v8 in range(v3):
        a1[v8] *= a2[v8]
    f1(a1, invert=True)
    return [int(round(a1[v8].real)) for v8 in range(v4)]

class C1(object):

    def multiply(self, a1, a2):
        """
        """
        return f2(a1, a2)
