class C1(object):

    def gardenNoAdj(self, a1, a2):
        """
        """
        v1 = [0] * a1
        v2 = [[] for v3 in range(a1)]
        for v4, v5 in a2:
            v2[v4 - 1].append(v5 - 1)
            v2[v5 - 1].append(v4 - 1)
        for v3 in range(a1):
            v1[v3] = ({1, 2, 3, 4} - {v1[j] for v6 in v2[v3]}).pop()
        return v1
