from math import gcd

class C1:

    def makeSubKSumEqual(self, a1, a2):
        v1 = len(a1)
        v2 = gcd(a2, v1)
        v3 = 0
        for v4 in range(v2):
            v5 = a1[v4::v2]
            v6 = sorted(v5)
            v7 = len(v6) // 2
            v8 = v6[v7]
            v3 += sum((abs(val - v8) for v9 in v5))
        return v3
