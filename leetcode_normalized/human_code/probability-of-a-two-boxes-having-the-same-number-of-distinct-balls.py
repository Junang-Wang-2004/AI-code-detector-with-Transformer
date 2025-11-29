import collections

class C1(object):

    def getProbability(self, a1):
        """
        """

        def nCrs(a1):
            v1 = 1
            for v2 in range(a1 + 1):
                yield v1
                v1 *= a1 - (v2 + 1) + 1
                v1 //= v2 + 1

        def nCr(a1, a2):
            if a1 - a2 < a2:
                return nCr(a1, a1 - a2)
            v1 = 1
            for v2 in range(1, a2 + 1):
                v1 *= a1 - v2 + 1
                v1 //= v2
            return v1
        v1 = collections.defaultdict(int)
        v1[0, 0] = 1
        for v2 in a1:
            v3 = collections.defaultdict(int)
            for (v4, v5), v6 in v1.items():
                for v7, v8 in enumerate(nCrs(v2)):
                    v9 = v4 + (v7 - (v2 - v7))
                    v10 = v5 - 1 if v7 == 0 else v5 + 1 if v7 == v2 else v5
                    v3[v9, v10] += v6 * v8
            v1 = v3
        v11 = sum(a1)
        return float(v1[0, 0]) / nCr(v11, v11 // 2)
