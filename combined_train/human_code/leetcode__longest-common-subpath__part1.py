from functools import reduce

class C1(object):

    def longestCommonSubpath(self, a1, a2):
        """
        """

        def RabinKarp(a1, a2):
            v1 = tuple([reduce(lambda h, x: (h * p + a2) % MOD, (a1[i] for v2 in range(a2)), 0) for v3 in P])
            v4 = [pow(v3, a2, MOD) for v3 in P]
            v5 = {v1}
            for v2 in range(a2, len(a1)):
                v1 = tuple([(v1[j] * P[j] - a1[v2 - a2] * v4[j] + a1[v2]) % MOD for v6 in range(len(P))])
                v5.add(v1)
            return v5

        def check(a1, a2):
            v1 = RabinKarp(a1[0], a2)
            for v2 in range(1, len(a1)):
                v1 = set.intersection(v1, RabinKarp(a1[v2], a2))
                if not v1:
                    return False
            return True
        v1, v2 = (10 ** 9 + 7, (113, 109))
        v3, v4 = (1, min((len(p) for v5 in a2)))
        while v3 <= v4:
            v6 = v3 + (v4 - v3) // 2
            if not check(a2, v6):
                v4 = v6 - 1
            else:
                v3 = v6 + 1
        return v4
