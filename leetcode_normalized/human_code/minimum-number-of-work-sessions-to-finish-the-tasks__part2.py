class C1(object):

    def minSessions(self, a1, a2):
        """
        """
        v1 = [[float('inf')] * 2 for v2 in range(1 << len(a1))]
        v1[0] = [0, a2]
        for v3 in range(len(v1) - 1):
            v4 = 1
            for v5 in a1:
                v6 = v3 | v4
                v4 <<= 1
                if v6 == v3:
                    continue
                if v1[v3][1] + v5 <= a2:
                    v1[v6] = min(v1[v6], [v1[v3][0], v1[v3][1] + v5])
                else:
                    v1[v6] = min(v1[v6], [v1[v3][0] + 1, v5])
        return v1[-1][0]
