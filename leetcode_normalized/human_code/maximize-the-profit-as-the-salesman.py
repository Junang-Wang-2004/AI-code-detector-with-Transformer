class C1(object):

    def maximizeTheProfit(self, a1, a2):
        """
        """
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v4].append([v3, v5])
        v6 = [0] * (a1 + 1)
        for v4 in range(a1):
            v6[v4 + 1] = v6[v4 - 1 + 1]
            for v3, v5 in v1[v4]:
                v6[v4 + 1] = max(v6[v4 + 1], v6[v3 - 1 + 1] + v5)
        return v6[-1]
