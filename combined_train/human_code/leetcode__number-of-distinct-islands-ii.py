class C1(object):

    def numDistinctIslands2(self, a1):
        """
        """
        v1 = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(a1, a2, a3, a4):
            if not (0 <= a1 < len(a3) and 0 <= a2 < len(a3[0]) and (a3[a1][a2] > 0)):
                return False
            a3[a1][a2] *= -1
            a4.append((a1, a2))
            for v1 in v1:
                dfs(a1 + v1[0], a2 + v1[1], a3, a4)
            return True

        def normalize(a1):
            v1 = [[] for v2 in range(8)]
            for v3, v4 in a1:
                v5 = [[v3, v4], [v3, -v4], [-v3, v4], [-v3, -v4], [v4, v3], [v4, -v3], [-v4, v3], [-v4, -v3]]
                for v6 in range(len(v5)):
                    v1[v6].append(v5[v6])
            for v7 in v1:
                v7.sort()
                v8 = list(v7[0])
                for v9 in v7:
                    v9[0] -= v8[0]
                    v9[1] -= v8[1]
            return min(v1)
        v2 = set()
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                v5 = []
                if dfs(v3, v4, a1, v5):
                    v2.add(str(normalize(v5)))
        return len(v2)
