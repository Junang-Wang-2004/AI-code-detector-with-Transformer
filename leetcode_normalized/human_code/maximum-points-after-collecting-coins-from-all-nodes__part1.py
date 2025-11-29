class C1(object):

    def maximumPoints(self, a1, a2, a3):
        """
        """
        v1 = float('-inf')

        def dfs(a1, a2, a3):
            if a3 >= max_base:
                return 0
            if lookup[a1] & a3:
                return v1
            lookup[a1] |= a3
            return max(a2[a1] // a3 - a3 + sum((dfs(v, a1, a3) for v1 in adj[a1] if v1 != a2)), a2[a1] // (a3 << 1) + sum((dfs(v1, a1, a3 << 1) for v1 in adj[a1] if v1 != a2)) if a2[a1] // a3 - a3 < a2[a1] // (a3 * 2) else v1)
        v2 = [[] for v3 in range(len(a2))]
        for v4, v5 in a1:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = 1 << max(a2).bit_length()
        v7 = [0] * len(a2)
        return dfs(0, -1, 1)
