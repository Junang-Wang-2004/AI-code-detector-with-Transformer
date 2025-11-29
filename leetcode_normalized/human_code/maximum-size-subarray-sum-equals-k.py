class C1(object):

    def maxSubArrayLen(self, a1, a2):
        """
        """
        v1 = {}
        v2, v3 = (0, 0)
        for v4 in range(len(a1)):
            v2 += a1[v4]
            if v2 == a2:
                v3 = v4 + 1
            elif v2 - a2 in v1:
                v3 = max(v3, v4 - v1[v2 - a2])
            if v2 not in v1:
                v1[v2] = v4
        return v3
