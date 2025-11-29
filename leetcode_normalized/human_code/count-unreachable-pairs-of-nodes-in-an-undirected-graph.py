class C1(object):

    def countPairs(self, a1, a2):
        """
        """

        def bfs(a1, a2, a3):
            v1 = [a2]
            a3[a2] = 1
            v2 = 1
            while v1:
                v3 = []
                for a2 in v1:
                    for v5 in a1[a2]:
                        if a3[v5]:
                            continue
                        a3[v5] = 1
                        v2 += 1
                        v3.append(v5)
                v1 = v3
            return v2
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0] * a1
        v6 = 0
        for v3 in range(a1):
            if v5[v3]:
                continue
            v7 = bfs(v1, v3, v5)
            v6 += v7 * (a1 - v7)
            a1 -= v7
        return v6
