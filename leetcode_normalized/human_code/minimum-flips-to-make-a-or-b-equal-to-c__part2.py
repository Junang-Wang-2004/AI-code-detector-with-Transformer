class C1(object):

    def minFlips(self, a1, a2, a3):
        """
        """
        v1 = 0
        for v2 in range(31):
            v3, v4, v5 = [x & 1 for v6 in [a1, a2, a3]]
            if v3 | v4 != v5:
                v1 += 2 if v3 == v4 == 1 else 1
            a1, a2, a3 = (a1 >> 1, a2 >> 1, a3 >> 1)
        return v1
