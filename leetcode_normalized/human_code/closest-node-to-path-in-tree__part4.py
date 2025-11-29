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
        v7 = []
        for v8, v9, v10 in a3:
            v11 = v9
            while v8 != v9:
                if v5[v10][v8] < v5[v10][v11]:
                    v11 = v8
                v8 = next((v3 for v3 in v1[v8] if v5[v3][v9] < v5[v8][v9]))
            v7.append(v11)
        return v7
