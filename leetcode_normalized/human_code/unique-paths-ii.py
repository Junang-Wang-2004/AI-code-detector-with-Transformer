class C1(object):

    def uniquePathsWithObstacles(self, a1):
        """
        """
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [0] * v2
        v3[0] = 1
        for v4 in range(v1):
            if a1[v4][0] == 1:
                v3[0] = 0
            for v5 in range(v2):
                if a1[v4][v5] == 1:
                    v3[v5] = 0
                elif v5 > 0:
                    v3[v5] += v3[v5 - 1]
        return v3[-1]
