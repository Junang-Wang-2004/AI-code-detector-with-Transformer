class C1(object):

    def countArrays(self, a1, a2):
        v1 = len(a1)
        v2, v3 = a2[0]
        v4 = 0
        for v5 in range(1, v1):
            v6 = a1[v5] - a1[v5 - 1]
            v4 += v6
            v2 = max(v2, a2[v5][0] - v4)
            v3 = min(v3, a2[v5][1] - v4)
        return max(0, v3 - v2 + 1)
