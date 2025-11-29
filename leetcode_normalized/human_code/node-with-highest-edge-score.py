class C1(object):

    def edgeScore(self, a1):
        """
        """
        v1 = [0] * len(a1)
        for v2, v3 in enumerate(a1):
            v1[v3] += v2
        return max(range(len(a1)), key=lambda x: v1[x])
