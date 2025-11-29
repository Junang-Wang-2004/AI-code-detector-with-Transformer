class C1(object):

    def twoEggDrop(self, a1):
        """
        """
        v1 = 2
        v2 = [[float('inf') for v3 in range(a1 + 1)] for v4 in range(2)]
        v2[1] = [v3 for v3 in range(a1 + 1)]
        for v5 in range(2, v1 + 1):
            v2[v5 % 2][0] = 0
            for v3 in range(1, a1 + 1):
                for v6 in range(1, v3 + 1):
                    v2[v5 % 2][v3] = min(v2[v5 % 2][v3], 1 + max(v2[(v5 - 1) % 2][v6 - 1], v2[v5 % 2][v3 - v6]))
        return v2[v1 % 2][a1]
