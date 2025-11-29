class C1(object):

    def findValidSplit(self, a1):

        def get_factors(a1):
            v1 = []
            v2 = 2
            while v2 * v2 <= a1:
                v3 = 0
                while a1 % v2 == 0:
                    a1 //= v2
                    v3 += 1
                if v3 > 0:
                    v1.append((v2, v3))
                v2 += 1 if v2 == 2 else 2
            if a1 > 1:
                v1.append((a1, 1))
            return v1
        v1 = len(a1)
        v2 = {}
        for v3 in range(v1 - 1, -1, -1):
            for v4, v5 in get_factors(a1[v3]):
                if v4 not in v2:
                    v2[v4] = v3
        v6 = -1
        for v7 in range(v1 - 1):
            for v4, v5 in get_factors(a1[v7]):
                if v4 in v2:
                    v6 = max(v6, v2[v4])
            if v6 <= v7:
                return v7
        return -1
