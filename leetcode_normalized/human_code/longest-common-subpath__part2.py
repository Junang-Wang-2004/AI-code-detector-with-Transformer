from functools import reduce

class C1(object):

    def longestCommonSubpath(self, a1, a2):
        """
        """

        def RabinKarp(a1, a2):
            v1 = reduce(lambda h, x: (v1 * P + a2) % MOD, (a1[i] for v2 in range(a2)), 0)
            v3 = pow(P, a2, MOD)
            v4 = {v1}
            for v2 in range(a2, len(a1)):
                v1 = (v1 * P - a1[v2 - a2] * v3 + a1[v2]) % MOD
                v4.add(v1)
            return v4

        def check(a1, a2):
            v1 = RabinKarp(a1[0], a2)
            for v2 in range(1, len(a1)):
                v1 = set.intersection(v1, RabinKarp(a1[v2], a2))
                if not v1:
                    return False
            return True
        v1, v2 = (10 ** 11 + 19, max((x for v3 in a2 for v4 in v3)) + 1)
        v5, v6 = (1, min((len(v3) for v3 in a2)))
        while v5 <= v6:
            v7 = v5 + (v6 - v5) // 2
            if not check(a2, v7):
                v6 = v7 - 1
            else:
                v5 = v7 + 1
        return v6
