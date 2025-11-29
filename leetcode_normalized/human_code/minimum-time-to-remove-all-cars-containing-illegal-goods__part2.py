class C1(object):

    def minimumTime(self, a1):
        """
        """
        v1, v2 = (len(a1), [0] * (len(a1) + 1))
        for v3 in reversed(range(len(a1))):
            v2[v3] = min(v2[v3 + 1] + 2 * (a1[v3] == '1'), len(a1) - v3)
        v4 = 0
        v1 = v4 + v2[0]
        for v3 in range(1, len(a1) + 1):
            v4 = min(v4 + 2 * (a1[v3 - 1] == '1'), v3)
            v1 = min(v1, v4 + v2[v3])
        return v1
