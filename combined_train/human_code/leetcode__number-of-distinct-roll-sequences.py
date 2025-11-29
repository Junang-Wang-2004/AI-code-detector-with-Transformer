import collections

class C1(object):

    def distinctSequences(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        if a1 == 1:
            return 6
        v1 = 10 ** 9 + 7
        v2 = [[0] * 6 for v3 in range(6)]
        for v4 in range(6):
            for v5 in range(6):
                if v4 != v5 and gcd(v4 + 1, v5 + 1) == 1:
                    v2[v4][v5] = 1
        for v3 in range(a1 - 2):
            v6 = [[0] * 6 for v3 in range(6)]
            for v4 in range(6):
                for v5 in range(6):
                    if not v2[v4][v5]:
                        continue
                    for v7 in range(6):
                        if not v2[v5][v7]:
                            continue
                        if v7 != v4:
                            v6[v4][v5] = (v6[v4][v5] + v2[v5][v7]) % v1
            v2 = v6
        return sum((v2[v4][v5] for v4 in range(6) for v5 in range(6))) % v1
