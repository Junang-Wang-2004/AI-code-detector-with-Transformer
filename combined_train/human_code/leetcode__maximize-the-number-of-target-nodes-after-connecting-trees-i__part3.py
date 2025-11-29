class C1(object):

    def maxTargetNodes(self, a1, a2, a3):
        """
        """

        def bfs(a1, a2, a3):
            v1 = 0
            v2 = [(a1, -1)]
            while v2:
                if a3 == -1:
                    break
                a3 -= 1
                v4 = []
                v1 += len(v2)
                for a1, v6 in v2:
                    for v7 in a2[a1]:
                        if v7 == v6:
                            continue
                        v4.append((v7, a1))
                v2 = v4
            return v1

        def find_adj(a1):
            v1 = [[] for v2 in range(len(a1) + 1)]
            for v3, v4 in a1:
                v1[v3].append(v4)
                v1[v4].append(v3)
            return v1
        v1 = find_adj(a2)
        v2 = max((bfs(u, v1, a3 - 1) for v3 in range(len(v1))))
        v4 = find_adj(a1)
        return [v2 + bfs(v3, v4, a3) for v3 in range(len(v4))]
