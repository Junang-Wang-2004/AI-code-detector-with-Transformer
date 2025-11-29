class C1(object):

    def calculateMinimumHP(self, a1):
        v1 = [float('inf') for v2 in a1[0]]
        v1[-1] = 1
        for v3 in reversed(range(len(a1))):
            v1[-1] = max(v1[-1] - a1[v3][-1], 1)
            for v4 in reversed(range(len(a1[v3]) - 1)):
                v5 = min(v1[v4], v1[v4 + 1])
                v1[v4] = max(v5 - a1[v3][v4], 1)
        return v1[0]
