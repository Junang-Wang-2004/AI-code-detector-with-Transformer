import collections

class C1(object):

    def distinctSubarraysWithAtMostKOddIntegers(self, a1, a2):

        def countDistinct(a1, a2, a3, a4):
            v1 = 0
            for v2 in reversed(range(a2, a3 + 1)):
                if a1[v2] not in a4:
                    v1 += 1
                a4 = a4[a1[v2]]
            return v1
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        v3, v4, v5 = (0, 0, 0)
        for v6 in range(len(a1)):
            v5 += a1[v6] % 2
            while v5 > a2:
                v5 -= a1[v4] % 2
                v4 += 1
            v3 += countDistinct(a1, v4, v6, v2)
        return v3
