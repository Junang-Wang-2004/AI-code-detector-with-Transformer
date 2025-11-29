from sortedcontainers import SortedList

class C1(object):

    def kthSmallest(self, a1, a2, a3):
        """
        """

        def small_to_large_merge(a1, a2):
            if len(a1) < len(a2):
                a1, a2 = (a2, a1)
            for v3 in a2:
                if v3 not in a1:
                    a1.add(v3)
            return a1

        def dfs(a1, a2):
            a2 ^= a2[a1]
            v2 = SortedList([a2])
            for v3 in adj[a1]:
                v2 = small_to_large_merge(v2, dfs(v3, a2))
            for v4 in lookup[a1]:
                if a3[v4][1] - 1 < len(v2):
                    result[v4] = v2[a3[v4][1] - 1]
            return v2
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4 in enumerate(a1):
            if v4 != -1:
                v1[v4].append(v3)
        v5 = [[] for v2 in range(len(v1))]
        for v6, (v3, v2) in enumerate(a3):
            v5[v3].append(v6)
        v7 = [-1] * len(a3)
        dfs(0, 0)
        return v7
