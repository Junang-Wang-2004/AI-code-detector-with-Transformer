class C1(object):

    def longestWPI(self, a1):
        """
        """
        v1, v2 = (0, 0)
        v3 = {}
        for v4, v5 in enumerate(a1):
            v2 = v2 + 1 if v5 > 8 else v2 - 1
            if v2 > 0:
                v1 = v4 + 1
            elif v2 - 1 in v3:
                v1 = max(v1, v4 - v3[v2 - 1])
            v3.setdefault(v2, v4)
        return v1
