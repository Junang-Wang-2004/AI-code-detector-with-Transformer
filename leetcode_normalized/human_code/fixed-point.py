class C1(object):

    def fixedPoint(self, a1):
        """
        """
        v1, v2 = (0, len(a1) - 1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if a1[v3] >= v3:
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1 if a1[v1] == v1 else -1
