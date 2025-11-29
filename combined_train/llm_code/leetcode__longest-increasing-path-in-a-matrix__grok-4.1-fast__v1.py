class C1(object):

    def longestIncreasingPath(self, a1):
        if not a1:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = {}

        def compute_length(a1, a2):
            v1 = (a1, a2)
            if v1 in v3:
                return v3[v1]
            v2 = 1
            for v3, v4 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                v5 = a1 + v3
                v6 = a2 + v4
                if 0 <= v5 < v1 and 0 <= v6 < v2 and (a1[v5][v6] > a1[a1][a2]):
                    v2 = max(v2, 1 + compute_length(v5, v6))
            v3[v1] = v2
            return v2
        v4 = 0
        for v5 in range(v1):
            for v6 in range(v2):
                v4 = max(v4, compute_length(v5, v6))
        return v4
