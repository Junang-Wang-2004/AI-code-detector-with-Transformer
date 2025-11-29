class C1(object):

    def shortestDistanceColor(self, a1, a2):
        """
        """
        v1 = [[-1 for v2 in range(len(a1))] for v2 in range(3)]
        v1[a1[0] - 1][0] = 0
        for v3 in range(1, len(a1)):
            for v4 in range(3):
                v1[v4][v3] = v1[v4][v3 - 1]
            v1[a1[v3] - 1][v3] = v3
        v1[a1[len(a1) - 1] - 1][len(a1) - 1] = len(a1) - 1
        for v3 in reversed(range(len(a1) - 1)):
            for v4 in range(3):
                if v1[v4][v3 + 1] == -1:
                    continue
                if v1[v4][v3] == -1 or abs(v1[v4][v3 + 1] - v3) < abs(v1[v4][v3] - v3):
                    v1[v4][v3] = v1[v4][v3 + 1]
            v1[a1[v3] - 1][v3] = v3
        return [abs(v1[v4 - 1][v3] - v3) if v1[v4 - 1][v3] != -1 else -1 for v3, v4 in a2]
