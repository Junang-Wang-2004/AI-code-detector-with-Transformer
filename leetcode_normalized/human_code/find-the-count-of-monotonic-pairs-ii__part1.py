from functools import reduce

class C1(object):

    def countOfPairs(self, a1):
        """
        """
        v1, v2, v3 = [[1] * 2 for v4 in range(3)]

        def nCr(a1, a2):
            while len(v2) <= a1:
                v1.append(v1[-1] * len(v2) % MOD)
                v2.append(v2[MOD % len(v2)] * (MOD - MOD // len(v2)) % MOD)
                v3.append(v3[-1] * v2[-1] % MOD)
            return v1[a1] * v3[a1 - a2] % MOD * v3[a2] % MOD

        def nHr(a1, a2):
            return nCr(a1 + a2 - 1, a2)
        v5 = 10 ** 9 + 7
        v6 = a1[-1] - sum((max(a1[i] - a1[i - 1], 0) for v7 in range(1, len(a1))))
        return nHr(len(a1) + 1, v6) if v6 >= 0 else 0
