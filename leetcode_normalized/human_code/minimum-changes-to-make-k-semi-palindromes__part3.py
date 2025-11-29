class C1(object):

    def minimumChanges(self, a1, a2):
        """
        """

        def min_dist(a1, a2):
            return min((sum((a1[a1 + i] != a1[a2 - ((i // d + 1) * d - 1) + i % d] for v1 in range((a2 - a1 + 1) // 2))) for v2 in divisors[a2 - a1 + 1]))
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3 in range(1, len(v1)):
            for v4 in range(v3 + v3, len(v1), v3):
                v1[v4].append(v3)
        v5 = [[len(a1)] * (a2 + 1) for v2 in range(len(a1) + 1)]
        v5[0][0] = 0
        for v3 in range(len(a1)):
            for v4 in range(v3):
                v6 = min_dist(v4, v3)
                for v7 in range(a2):
                    v5[v3 + 1][v7 + 1] = min(v5[v3 + 1][v7 + 1], v5[v4][v7] + v6)
        return v5[len(a1)][a2]
