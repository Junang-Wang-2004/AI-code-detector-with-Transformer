class C1(object):

    def maxDifference(self, a1):
        """
        """
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3, v4 = (float('inf'), 0)
        for v2 in v1:
            if not v2:
                continue
            if v2 % 2 == 0:
                v3 = min(v3, v2)
            else:
                v4 = max(v4, v2)
        return v4 - v3
