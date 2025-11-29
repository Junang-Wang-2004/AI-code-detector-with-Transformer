class C1(object):

    def maxChunksToSorted(self, a1):
        """
        """

        def compare(a1, a2):
            return a1[a1] - a1[a2] if a1[a1] != a1[a2] else a1 - a2
        v1 = [i for v2 in range(len(a1))]
        v3, v4 = (0, 0)
        for v2, v5 in enumerate(sorted(v1, cmp=compare)):
            v4 = max(v4, v5)
            if v4 == v2:
                v3 += 1
        return v3
