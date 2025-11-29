class C1(object):

    def stoneGameVII(self, a1):
        """
        """

        def score(a1, a2):
            return prefix[a2 + 1] - prefix[a1]
        v1 = [0]
        for v2 in a1:
            v1.append(v1[-1] + v2)
        v3 = [[0 for v4 in range(len(a1))] for v4 in range(2)]
        for v5 in reversed(range(len(a1))):
            for v6 in range(v5 + 1, len(a1)):
                v3[v5 % 2][v6] = max(score(v5 + 1, v6) - v3[(v5 + 1) % 2][v6], score(v5, v6 - 1) - v3[v5 % 2][v6 - 1])
        return v3[0][-1]
