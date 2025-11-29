class C1(object):

    def rob(self, a1):
        if len(a1) == 0:
            return 0
        if len(a1) == 1:
            return a1[0]
        return max(self.robRange(a1, 0, len(a1) - 1), self.robRange(a1, 1, len(a1)))

    def robRange(self, a1, a2, a3):
        v1, v2 = (a1[a2], 0)
        for v3 in range(a2 + 1, a3):
            v2, v4 = (v1, v2)
            v1 = max(a1[v3] + v4, v2)
        return v1
