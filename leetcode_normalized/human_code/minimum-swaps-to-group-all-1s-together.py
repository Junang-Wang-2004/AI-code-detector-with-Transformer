class C1(object):

    def minSwaps(self, a1):
        """
        """
        v1 = sum(a1)
        v2, v3, v4 = (0, 0, 0)
        for v5 in range(len(a1)):
            v3 += a1[v5]
            if v5 - v4 + 1 > v1:
                v3 -= a1[v4]
                v4 += 1
            v2 = max(v2, v3)
        return v1 - v2
