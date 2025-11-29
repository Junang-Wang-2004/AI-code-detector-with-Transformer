class C1(object):

    def findKDistantIndices(self, a1, a2, a3):
        """
        """
        v1 = []
        v2 = -1
        for v3, v4 in enumerate(a1):
            if v4 != a2:
                continue
            for v5 in range(max(v3 - a3, v2 + 1), min(v3 + a3 + 1, len(a1))):
                v1.append(v5)
            v2 = min(v3 + a3, len(a1) - 1)
        return v1
