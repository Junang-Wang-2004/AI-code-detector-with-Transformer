class C1(object):

    def findLengthOfShortestSubarray(self, a1):
        """
        """
        v1 = -1
        for v1 in reversed(range(1, len(a1))):
            if a1[v1 - 1] > a1[v1]:
                break
        else:
            return 0
        v2 = v1
        for v3 in range(v1):
            if v3 and a1[v3] < a1[v3 - 1]:
                break
            while v1 < len(a1) and a1[v3] > a1[v1]:
                v1 += 1
            v2 = min(v2, v1 - v3 + 1 - 2)
        return v2
