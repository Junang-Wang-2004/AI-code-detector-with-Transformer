class C1(object):

    def distinctSubarraysWithAtMostKOddIntegers(self, a1, a2):

        def countDistinct(a1, a2, a3, a4):
            v1 = 0
            for v2 in range(a2, a3 + 1):
                if a1[v2] not in a4:
                    v1 += 1
                a4 = a4[a1[v2]]
            return v1
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        v3 = 0
        for v4 in range(len(a1)):
            v5 = 0
            for v6 in range(v4, len(a1)):
                v5 += a1[v6] % 2
                if v5 > a2:
                    v6 -= 1
                    break
            v3 += countDistinct(a1, v4, v6, v2)
        return v3
