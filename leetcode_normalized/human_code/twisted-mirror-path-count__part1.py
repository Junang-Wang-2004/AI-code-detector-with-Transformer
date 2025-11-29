class C1(object):

    def uniquePaths(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        def get(a1, a2):
            return a1[a1][a2] if len(a1) > len(a1[0]) else a1[a2][a1]
        v2 = [[0] * 2 for v3 in range(min(len(a1), len(a1[0])) + 1)]
        v2[1] = [1] * 2
        for v4 in range(max(len(a1), len(a1[0]))):
            for v5 in range(len(v2) - 1):
                if get(v4, v5):
                    v2[v5 + 1] = [v2[v5 + 1][1], v2[v5][0]]
                else:
                    v2[v5 + 1] = [(v2[v5 + 1][1] + v2[v5][0]) % v1] * 2
        return v2[-1][0]
