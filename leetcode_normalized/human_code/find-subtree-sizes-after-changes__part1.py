class C1(object):

    def findSubtreeSizes(self, a1, a2):
        """
        """

        def iter_dfs():
            v1 = [[] for v2 in range(26)]
            v3 = [1] * len(a1)
            v4 = [(1, 0)]
            while v4:
                v5, v6 = v4.pop()
                if v5 == 1:
                    v1[ord(a2[v6]) - ord('a')].append(v6)
                    v4.append((2, v6))
                    for v7 in reversed(adj[v6]):
                        v4.append((1, v7))
                elif v5 == 2:
                    for v7 in adj[v6]:
                        v3[v1[ord(a2[v7]) - ord('a')][-1] if v1[ord(a2[v7]) - ord('a')] else v6] += v3[v7]
                    v1[ord(a2[v6]) - ord('a')].pop()
            return v3
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4 in enumerate(a1):
            if v4 != -1:
                v1[v4].append(v3)
        return iter_dfs()
