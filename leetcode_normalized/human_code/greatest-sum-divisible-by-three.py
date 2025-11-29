class C1(object):

    def maxSumDivThree(self, a1):
        """
        """
        v1 = [0, 0, 0]
        for v2 in a1:
            for v3 in [v2 + x for v4 in v1]:
                v1[v3 % 3] = max(v1[v3 % 3], v3)
        return v1[0]
