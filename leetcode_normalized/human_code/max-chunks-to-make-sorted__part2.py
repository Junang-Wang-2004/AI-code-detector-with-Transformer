class C1(object):

    def maxChunksToSorted(self, a1):
        """
        """
        v1, v2 = (0, [])
        for v3 in a1:
            v4 = v3 if not v2 else max(v2[-1], v3)
            while v2 and v2[-1] > v3:
                v2.pop()
            v2.append(v4)
        return len(v2)
