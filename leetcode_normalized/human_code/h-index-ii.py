class C1(object):

    def hIndex(self, a1):
        """
        """
        v1 = len(a1)
        v2, v3 = (0, v1 - 1)
        while v2 <= v3:
            v4 = (v2 + v3) / 2
            if a1[v4] >= v1 - v4:
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return v1 - v2
