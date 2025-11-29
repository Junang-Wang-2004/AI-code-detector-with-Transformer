class C1(object):

    def maxPrice(self, a1, a2):
        """
        """
        v1 = 0
        a1.sort(key=lambda x: float(x[0]) / x[1], reverse=True)
        for v2, v3 in a1:
            v4 = min(v3, a2)
            a2 -= v4
            v1 += float(v2) / v3 * v4
        return v1 if a2 == 0 else -1
