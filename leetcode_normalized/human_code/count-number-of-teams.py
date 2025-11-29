class C1(object):

    def numTeams(self, a1):
        """
        """
        v1 = 0
        for v2 in range(1, len(a1) - 1):
            v3, v4 = ([0] * 2, [0] * 2)
            for v5 in range(len(a1)):
                if a1[v2] > a1[v5]:
                    v3[v2 < v5] += 1
                if a1[v2] < a1[v5]:
                    v4[v2 < v5] += 1
            v1 += v3[0] * v4[1] + v4[0] * v3[1]
        return v1
