class C1(object):

    def trap(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = 0
        for v3 in reversed(range(len(a1))):
            v1[v3] = v2
            v2 = max(v2, a1[v3])
        v4 = v5 = 0
        for v3 in range(len(a1)):
            v5 = max(v5, a1[v3])
            v4 += max(min(v5, v1[v3]) - a1[v3], 0)
        return v4
