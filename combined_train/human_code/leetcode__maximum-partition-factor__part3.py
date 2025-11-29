class C1(object):

    def maxPartitionFactor(self, a1):
        """
        """
        v1 = float('inf')

        def binary_search_right(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if not a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a2

        def dist(a1, a2):
            return abs(a1[a1][0] - a1[a2][0]) + abs(a1[a1][1] - a1[a2][1])

        def is_bipartite(a1):

            def bfs(a1):
                if lookup[a1] != -1:
                    return True
                lookup[a1] = 0
                v1 = [a1]
                while v1:
                    v2 = []
                    for a1 in v1:
                        for v4 in range(len(a1)):
                            if not (v4 != a1 and dist(v4, a1) < a1):
                                continue
                            if lookup[v4] != -1:
                                if lookup[v4] != lookup[a1] ^ 1:
                                    return False
                                continue
                            lookup[v4] = lookup[a1] ^ 1
                            v2.append(v4)
                    v1 = v2
                return True
            v1 = [-1] * len(a1)
            return all((bfs(u) for v2 in range(len(a1))))
        v2 = sorted({dist(u, v) for v3 in range(len(a1)) for v4 in range(v3 + 1, len(a1))} | {v1})
        v5, v6 = (0, len(v2) - 1)
        v7 = binary_search_right(v5, v6, lambda i: is_bipartite(v2[i]))
        return v2[v7] if v2[v7] != v1 else 0
