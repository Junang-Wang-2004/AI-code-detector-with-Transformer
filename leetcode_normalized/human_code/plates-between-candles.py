class C1(object):

    def platesBetweenCandles(self, a1, a2):
        """
        """
        v1, v2 = ([0] * len(a1), {})
        v3, v4 = (-1, 0)
        for v5 in range(len(a1)):
            if a1[v5] == '|':
                v3 = v5
                v4 += 1
                v2[v5] = v4
            v1[v5] = v3
        v6 = [0] * len(a1)
        v3 = len(a1)
        for v5 in reversed(range(len(a1))):
            if a1[v5] == '|':
                v3 = v5
            v6[v5] = v3
        return [max(v1[r] - v6[l] + 1 - (v2[v1[r]] - v2[v6[l]] + 1), 0) for v7, v8 in a2]
