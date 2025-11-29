class C1(object):

    def maxDistinctElements(self, a1, a2):
        """
        """
        v1 = 0
        a1.sort()
        v2 = float('-inf')
        for v3 in a1:
            if v2 > v3 + a2:
                continue
            v2 = max(v2, v3 - a2) + 1
            v1 += 1
        return v1
