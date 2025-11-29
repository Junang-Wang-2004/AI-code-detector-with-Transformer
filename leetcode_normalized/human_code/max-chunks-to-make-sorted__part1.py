class C1(object):

    def maxChunksToSorted(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3, v4 in enumerate(a1):
            v2 = max(v2, v4)
            if v2 == v3:
                v1 += 1
        return v1
