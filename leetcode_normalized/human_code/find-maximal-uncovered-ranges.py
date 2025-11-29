class C1(object):

    def findMaximalUncoveredRanges(self, a1, a2):
        """
        """
        a2.sort()
        v1 = [[-1, -1]]
        for v2, v3 in a2:
            if v1[-1][1] < v2:
                v1.append([v2, v3])
                continue
            v1[-1][1] = max(v1[-1][1], v3)
        v1.append([a1, a1])
        return [[v1[i - 1][1] + 1, v1[i][0] - 1] for v4 in range(1, len(v1)) if v1[v4 - 1][1] + 1 <= v1[v4][0] - 1]
