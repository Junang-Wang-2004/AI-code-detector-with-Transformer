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

        def iter_dfs():
            v1 = [SortedList() for v2 in range(len(adj))]
            v3 = [-1] * len(a3)
            v4 = [(1, (0, 0))]
            while v4:
                v5, (v6, v7) = v4.pop()
                if v5 == 1:
                    v7 ^= a2[v6]
                    v1[v6].add(v7)
                    v4.append((2, (v6, v7)))
                    for v8 in reversed(adj[v6]):
                        v4.append((1, (v8, v7)))
                elif v5 == 2:
                    for v8 in adj[v6]:
                        v1[v6] = small_to_large_merge(v1[v6], v1[v8])
                    for v9 in lookup[v6]:
                        if a3[v9][1] - 1 < len(v1[v6]):
                            v3[v9] = v1[v6][a3[v9][1] - 1]
            return v3
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4 in enumerate(a1):
            if v4 != -1:
                v1[v4].append(v3)
        v5 = [[] for v2 in range(len(v1))]
        for v6, (v3, v2) in enumerate(a3):
            v5[v3].append(v6)
        return iter_dfs()
