class C1(object):

    def countCoveredBuildings(self, a1, a2):
        """
        """
        v1 = [a1] * a1
        v2 = [-1] * a1
        v3 = [-1] * a1
        v4 = [a1] * a1
        for v5, v6 in a2:
            v5 -= 1
            v6 -= 1
            v1[v6] = min(v1[v6], v5)
            v2[v6] = max(v2[v6], v5)
            v3[v5] = max(v3[v5], v6)
            v4[v5] = min(v4[v5], v6)
        return sum((v1[v6 - 1] < v5 - 1 < v2[v6 - 1] and v4[v5 - 1] < v6 - 1 < v3[v5 - 1] for v5, v6 in a2))
