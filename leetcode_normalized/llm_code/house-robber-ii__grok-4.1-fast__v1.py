class C1(object):

    def rob(self, a1):
        v1 = len(a1)
        if not a1:
            return 0
        if v1 == 1:
            return a1[0]
        v2, v3 = (0, a1[0])
        for v4 in range(1, v1 - 1):
            v5 = max(a1[v4] + v2, v3)
            v2 = v3
            v3 = v5
        v6 = v3
        v2, v3 = (0, a1[1])
        for v4 in range(2, v1):
            v5 = max(a1[v4] + v2, v3)
            v2 = v3
            v3 = v5
        v7 = v3
        return max(v6, v7)
