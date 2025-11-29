class C1(object):

    def findAnswer(self, a1, a2):
        """
        """

        def manacher(a1):
            a1 = '^#' + '#'.join(a1) + '#$'
            v2 = [0] * len(a1)
            v3, v4 = (0, 0)
            for v5 in range(1, len(a1) - 1):
                v6 = 2 * v3 - v5
                if v4 > v5:
                    v2[v5] = min(v4 - v5, v2[v6])
                while a1[v5 + 1 + v2[v5]] == a1[v5 - 1 - v2[v5]]:
                    v2[v5] += 1
                if v5 + v2[v5] > v4:
                    v3, v4 = (v5, v5 + v2[v5])
            return v2

        def dfs(a1):
            v1 = cnt[0]
            for v2 in adj[a1]:
                dfs(v2)
            curr.append(a2[a1])
            lookup[a1] = (v1, cnt[0])
            cnt[0] += 1
        v1 = [[] for v2 in range(len(a1))]
        for v3 in range(1, len(a1)):
            v1[a1[v3]].append(v3)
        v4 = [0]
        v5 = []
        v6 = [None] * len(v1)
        dfs(0)
        v7 = manacher(v5)
        return [v7[(2 * (left + 1) + 2 * (right + 1)) // 2] >= right - left + 1 for v8, v9 in v6]
