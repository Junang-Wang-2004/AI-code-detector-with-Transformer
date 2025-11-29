class C1(object):

    def countPoints(self, a1, a2):
        """
        """
        v1 = []
        for v2, v3, v4 in a2:
            v1.append(0)
            for v5, v6 in a1:
                if (v5 - v2) ** 2 + (v6 - v3) ** 2 <= v4 ** 2:
                    v1[-1] += 1
        return v1
