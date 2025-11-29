class C1(object):

    def maxBuilding(self, a1, a2):
        """
        """
        a2.extend([[1, 0], [a1, a1 - 1]])
        a2.sort()
        for v1 in reversed(range(len(a2) - 1)):
            a2[v1][1] = min(a2[v1][1], a2[v1 + 1][1] + (a2[v1 + 1][0] - a2[v1][0]))
        v2 = 0
        for v1 in range(1, len(a2)):
            a2[v1][1] = min(a2[v1][1], a2[v1 - 1][1] + (a2[v1][0] - a2[v1 - 1][0]))
            v3, v4 = a2[v1 - 1]
            v5, v6 = a2[v1]
            v2 = max(v2, max(v4, v6) + (v5 - v3 - abs(v4 - v6)) // 2)
        return v2
