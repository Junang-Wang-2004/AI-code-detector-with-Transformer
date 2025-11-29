class C1(object):

    def minProcessingTime(self, a1, a2):
        v1 = sorted(a1)
        v2 = sorted(a2, reverse=True)
        v3 = 0
        v4 = len(v1)
        for v5 in range(v4):
            v3 = max(v3, v1[v5] + v2[4 * v5])
        return v3
