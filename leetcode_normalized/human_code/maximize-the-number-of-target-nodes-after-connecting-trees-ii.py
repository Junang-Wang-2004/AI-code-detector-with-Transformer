class C1(object):

    def maxTargetNodes(self, a1, a2):
        """
        """

        def bfs(a1):
            v1 = [0] * len(a1)
            v2 = 0
            v3 = [-1] * len(a1)
            v3[0] = v2
            v4 = [0]
            while v4:
                v5 = []
                for v6 in v4:
                    for v7 in a1[v6]:
                        if v3[v7] != -1:
                            continue
                        v3[v7] = v2 ^ 1
                        v5.append(v7)
                v4 = v5
                v2 ^= 1
            v8 = sum(v3)
            return [v8 if v3[v6] else len(a1) - v8 for v6 in range(len(a1))]

        def find_adj(a1):
            v1 = [[] for v2 in range(len(a1) + 1)]
            for v3, v4 in a1:
                v1[v3].append(v4)
                v1[v4].append(v3)
            return v1
        v1 = find_adj(a2)
        v2 = max(bfs(v1))
        v3 = find_adj(a1)
        return [v2 + x for v4 in bfs(v3)]
