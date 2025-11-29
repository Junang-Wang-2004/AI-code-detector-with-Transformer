class C1(object):

    def findSubtreeSizes(self, a1, a2):
        """
        """

        def dfs(a1):
            lookup[ord(a2[a1]) - ord('a')].append(a1)
            for v1 in adj[a1]:
                dfs(v1)
                result[lookup[ord(a2[v1]) - ord('a')][-1] if lookup[ord(a2[v1]) - ord('a')] else a1] += result[v1]
            lookup[ord(a2[a1]) - ord('a')].pop()
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4 in enumerate(a1):
            if v4 != -1:
                v1[v4].append(v3)
        v5 = [[] for v2 in range(26)]
        v6 = [1] * len(a1)
        dfs(0)
        return v6
