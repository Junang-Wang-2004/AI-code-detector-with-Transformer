import collections

class C1(object):

    def minimumLines(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return abs(a1)

        def popcount(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2
        v1 = collections.defaultdict(set)
        for v2, (v3, v4) in enumerate(a1):
            for v5 in range(v2 + 1, len(a1)):
                v6, v7 = a1[v5]
                v8, v9 = (v6 - v3, v7 - v4)
                v10 = gcd(v8, v9)
                v11, v12 = (v8 // v10, v9 // v10)
                if v11 < 0 or (v11 == 0 and v12 < 0):
                    v11, v12 = (-v11, -v12)
                v13 = v12 * v3 - v11 * v4
                v1[v11, v12, v13].add((v3, v4))
                v1[v11, v12, v13].add((v6, v7))
        v14 = [l for v15, v16 in v1.items() if len(v16) > 2]
        assert len(v14) <= len(a1) // 2
        v17 = float('inf')
        for v18 in range(1 << len(v14)):
            v19 = set()
            v20, v2 = (1, 0)
            while v20 <= v18:
                if v18 & v20:
                    v19.update(v1[v14[v2]])
                v20 <<= 1
                v2 += 1
            v17 = min(v17, popcount(v18) + ceil_divide(len(a1) - len(v19), 2))
        return v17
