class C1(object):

    def minDamage(self, a1, a2, a3):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2
        v1 = list(range(len(a3)))
        v1.sort(key=lambda i: float(ceil_divide(a3[i], a1)) / a2[i])
        v2 = v3 = 0
        for v4 in v1:
            v3 += ceil_divide(a3[v4], a1)
            v2 += v3 * a2[v4]
        return v2
