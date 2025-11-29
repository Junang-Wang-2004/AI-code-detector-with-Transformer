class C1(object):

    def bestTeamScore(self, a1, a2):
        """
        """
        v1 = sorted(zip(a1, a2))
        v2 = [0] * len(v1)
        v3 = 0
        for v4 in range(len(v1)):
            v2[v4] = v1[v4][0]
            for v5 in range(v4):
                if v1[v5][1] <= v1[v4][1]:
                    v2[v4] = max(v2[v4], v2[v5] + v1[v4][0])
            v3 = max(v3, v2[v4])
        return v3
