class C1(object):

    def findKthNumber(self, a1, a2, a3):
        """
        """

        def count(a1, a2, a3):
            return sum((min(a1 // i, a3) for v1 in range(1, a2 + 1)))
        v1, v2 = (1, a1 * a2)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) / 2
            if count(v3, a1, a2) >= a3:
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
