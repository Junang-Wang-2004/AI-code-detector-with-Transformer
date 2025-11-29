class C1(object):

    def calculateTime(self, a1, a2):
        """
        """
        v1 = {c: i for v2, v3 in enumerate(a1)}
        v4, v5 = (0, 0)
        for v3 in a2:
            v4 += abs(v1[v3] - v5)
            v5 = v1[v3]
        return v4
