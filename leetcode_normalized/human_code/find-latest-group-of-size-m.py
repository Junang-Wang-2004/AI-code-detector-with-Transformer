class C1(object):

    def findLatestStep(self, a1, a2):
        """
        """
        if a2 == len(a1):
            return a2
        v1 = [0] * (len(a1) + 2)
        v2 = -1
        for v3, v4 in enumerate(a1):
            v5, v6 = (v1[v4 - 1], v1[v4 + 1])
            if v5 == a2 or v6 == a2:
                v2 = v3
            v1[v4 - v5] = v1[v4 + v6] = v5 + v6 + 1
        return v2
