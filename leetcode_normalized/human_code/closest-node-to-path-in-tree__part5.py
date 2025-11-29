class C1(object):

    def closestNode(self, a1, a2, a3):
        """
        """

        def bfs(a1, a2):
            v1 = [len(a1)] * len(a1)
            v2 = [a2]
            v1[a2] = 0
            v3 = 0
            while v2:
                v4 = []
                for v5 in v2:
                    for v6 in a1[v5]:
                        if v3 + 1 >= v1[v6]:
                            continue
                        v1[v6] = v3 + 1
                        v4.append(v6)
                v2 = v4
                v3 += 1
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            (v1[v3].append(v4), v1[v4].append(v3))
        v5 = [bfs(v1, i) for v6 in range(a1)]
        return [max((v6 for v6 in range(a1) if v5[start][node] + v5[node][end] - 2 * v5[node][v6] == v5[start][v6] + v5[v6][end]), key=lambda x: v5[node][x]) for v7, v8, v9 in a3]
