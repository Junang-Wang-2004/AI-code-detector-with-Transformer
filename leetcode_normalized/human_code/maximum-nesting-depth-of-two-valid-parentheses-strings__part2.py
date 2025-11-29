class C1(object):

    def maxDepthAfterSplit(self, a1):
        """
        """
        v1, v2 = (0, 0)
        v3 = [0] * len(a1)
        for v4, v5 in enumerate(a1):
            v6 = 1 if v5 == '(' else -1
            if v6 == 1 and v1 <= v2 or (v6 == -1 and v1 >= v2):
                v1 += v6
            else:
                v2 += v6
                v3[v4] = 1
        return v3
