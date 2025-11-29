class C1(object):

    def findNumberOfLIS(self, a1):
        """
        """
        v1, v2 = (0, 0)
        v3 = [[1, 1] for v4 in range(len(a1))]
        for v5 in range(len(a1)):
            for v6 in range(v5):
                if a1[v5] > a1[v6]:
                    if v3[v5][0] == v3[v6][0] + 1:
                        v3[v5][1] += v3[v6][1]
                    elif v3[v5][0] < v3[v6][0] + 1:
                        v3[v5] = [v3[v6][0] + 1, v3[v6][1]]
            if v2 == v3[v5][0]:
                v1 += v3[v5][1]
            elif v2 < v3[v5][0]:
                v2 = v3[v5][0]
                v1 = v3[v5][1]
        return v1
