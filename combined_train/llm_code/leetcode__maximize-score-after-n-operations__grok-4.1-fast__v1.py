from math import gcd

class C1:

    def maxScore(self, a1):
        v1 = len(a1)
        v2 = 1 << v1
        v3 = [0] * v2
        for v4 in range(v2):
            v5 = bin(v4).count('1')
            if v5 % 2 != 0 or v5 == 0:
                continue
            v6 = v5 // 2
            for v7 in range(v1):
                if v4 & 1 << v7 == 0:
                    continue
                for v8 in range(v7 + 1, v1):
                    if v4 & 1 << v8 == 0:
                        continue
                    v9 = v4 ^ 1 << v7 ^ 1 << v8
                    v10 = v6 * gcd(a1[v7], a1[v8]) + v3[v9]
                    if v10 > v3[v4]:
                        v3[v4] = v10
        return v3[v2 - 1]
