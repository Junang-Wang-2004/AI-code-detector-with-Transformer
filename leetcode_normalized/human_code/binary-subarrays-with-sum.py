class C1(object):

    def numSubarraysWithSum(self, a1, a2):
        """
        """
        v1 = 0
        v2, v3, v4, v5 = (0, 0, 0, 0)
        for v6, v7 in enumerate(a1):
            v4 += v7
            while v2 < v6 and v4 > a2:
                v4 -= a1[v2]
                v2 += 1
            v5 += v7
            while v3 < v6 and (v5 > a2 or (v5 == a2 and (not a1[v3]))):
                v5 -= a1[v3]
                v3 += 1
            if v4 == a2:
                v1 += v3 - v2 + 1
        return v1
