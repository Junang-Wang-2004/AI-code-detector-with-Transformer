class C1(object):

    def partitionString(self, a1):
        """
        """
        v1, v2 = (1, 0)
        v3 = {}
        for v4, v5 in enumerate(a1):
            if v5 in v3 and v3[v5] >= v2:
                v2 = v4
                v1 += 1
            v3[v5] = v4
        return v1
