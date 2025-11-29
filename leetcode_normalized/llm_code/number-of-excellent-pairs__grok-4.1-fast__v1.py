import bisect

class C1:

    def countExcellentPairs(self, a1, a2):

        def ones_count(a1):
            v1 = 0
            while a1:
                v1 += a1 & 1
                a1 >>= 1
            return v1
        v1 = sorted((ones_count(x) for v2 in a1))
        v3 = 0
        v4 = len(v1)
        for v5 in v1:
            v6 = a2 - v5
            v7 = bisect.bisect_left(v1, v6)
            v3 += v4 - v7
        return v3
