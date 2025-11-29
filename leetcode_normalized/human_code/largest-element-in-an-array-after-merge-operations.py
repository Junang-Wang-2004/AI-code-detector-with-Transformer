class C1(object):

    def maxArrayValue(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in reversed(range(len(a1))):
            if a1[v3] > v2:
                v2 = 0
            v2 += a1[v3]
            v1 = max(v1, v2)
        return v1
