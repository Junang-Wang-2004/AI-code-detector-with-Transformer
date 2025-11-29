class C1(object):

    def longestPath(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3, a4):
            v1 = [0] * 2
            for v2 in a2[a3]:
                v3 = dfs(a1, a2, v2, a4)
                if a1[v2] == a1[a3]:
                    continue
                if v3 > v1[0]:
                    v1[0], v1[1] = (v3, v1[0])
                elif v3 > v1[1]:
                    v1[1] = v3
            a4[0] = max(a4[0], v1[0] + v1[1] + 1)
            return v1[0] + 1
        v1 = [[] for v2 in range(len(a2))]
        for v3 in range(1, len(a1)):
            v1[a1[v3]].append(v3)
        v4 = [0]
        dfs(a2, v1, 0, v4)
        return v4[0]
