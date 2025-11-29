class C1(object):

    def numMagicSquaresInside(self, a1):
        """
        """

        def magic(a1, a2, a3):
            v1 = k * (k ** 2 + 1) // 2
            v2 = set()
            v3 = float('inf')
            v4, v5 = (0, 0)
            for v6 in range(k):
                v4 += a1[a2 + v6][a3 + v6]
                v5 += a1[a2 + v6][a3 + k - 1 - v6]
                v7, v8 = (0, 0)
                for v9 in range(k):
                    v3 = min(v3, a1[a2 + v6][a3 + v9])
                    v2.add(a1[a2 + v6][a3 + v9])
                    v7 += a1[a2 + v6][a3 + v9]
                    v8 += a1[a2 + v9][a3 + v6]
                if not v7 == v8 == v1:
                    return False
            return v4 == v5 == v1 and len(v2) == k ** 2 and (v3 == 1)
        v1 = 3
        v2 = 0
        for v3 in range(len(a1) - v1 + 1):
            for v4 in range(len(a1[v3]) - v1 + 1):
                if magic(a1, v3, v4):
                    v2 += 1
        return v2
