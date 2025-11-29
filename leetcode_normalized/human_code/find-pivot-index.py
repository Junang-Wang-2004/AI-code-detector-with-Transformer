class C1(object):

    def pivotIndex(self, a1):
        """
        """
        v1 = sum(a1)
        v2 = 0
        for v3, v4 in enumerate(a1):
            if v2 == v1 - v2 - v4:
                return v3
            v2 += v4
        return -1
