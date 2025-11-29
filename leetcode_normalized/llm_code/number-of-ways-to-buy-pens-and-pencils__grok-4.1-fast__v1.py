import math

class C1(object):

    def waysToBuyPensPencils(self, a1, a2, a3):
        v1 = max(a2, a3)
        v2 = min(a2, a3)
        v3 = math.gcd(v1, v2)
        v4 = v1 // v3 * v2
        v5 = v4 // v2
        v6 = a1 // v1 + 1
        v7 = min(v6, v5)
        v8 = 0
        for v9 in range(v7):
            v10 = a1 - v9 * v1
            v11 = v10 // v2 + 1
            v12 = (v11 + v5 - 1) // v5
            v13 = v11
            v14 = v11 - (v12 - 1) * v5
            v8 += v12 * (v13 + v14) // 2
        return v8
