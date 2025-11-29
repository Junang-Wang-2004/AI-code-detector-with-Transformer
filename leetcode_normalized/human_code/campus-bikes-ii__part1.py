class C1(object):

    def assignBikes(self, a1, a2):
        """
        """

        def manhattan(a1, a2):
            return abs(a1[0] - a2[0]) + abs(a1[1] - a2[1])
        v1 = [[float('inf')] * (1 << len(a2)) for v2 in range(2)]
        v1[0][0] = 0
        for v3 in range(len(a1)):
            v1[(v3 + 1) % 2] = [float('inf')] * (1 << len(a2))
            for v4 in range(len(a2)):
                for v5 in range(1 << len(a2)):
                    if v5 & 1 << v4:
                        continue
                    v1[(v3 + 1) % 2][v5 | 1 << v4] = min(v1[(v3 + 1) % 2][v5 | 1 << v4], v1[v3 % 2][v5] + manhattan(a1[v3], a2[v4]))
        return min(v1[len(a1) % 2])
