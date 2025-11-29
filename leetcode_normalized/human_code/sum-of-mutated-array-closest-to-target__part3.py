class C1(object):

    def findBestValue(self, a1, a2):
        """
        """

        def total(a1, a2):
            v1 = 0
            for v2 in a1:
                v1 += min(a2, v2)
            return v1

        def check(a1, a2, a3):
            return total(a1, a2) >= a3
        v1, v2 = (1, max(a1))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if check(a1, v3, a2):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1 - 1 if a2 - total(a1, v1 - 1) <= total(a1, v1) - a2 else v1
