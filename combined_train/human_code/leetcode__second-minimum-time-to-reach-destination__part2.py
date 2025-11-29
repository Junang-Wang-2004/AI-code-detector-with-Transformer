class C1(object):

    def secondMinimum(self, a1, a2, a3, a4):
        """
        """
        v1 = float('inf')

        def bfs(a1, a2):
            v1 = [a2]
            v2 = [v1] * len(a1)
            v2[a2] = 0
            while v1:
                v3 = []
                for v4 in v1:
                    for v5 in a1[v4]:
                        if v2[v5] != v1:
                            continue
                        v2[v5] = v2[v4] + 1
                        v3.append(v5)
                v1 = v3
            return v2

        def calc_time(a1, a2, a3):
            v1 = 0
            for v2 in range(a3):
                if v1 // a2 % 2:
                    v1 = (v1 // a2 + 1) * a2
                v1 += a1
            return v1
        v2 = [[] for v3 in range(a1)]
        for v4, v5 in a2:
            v2[v4 - 1].append(v5 - 1)
            v2[v5 - 1].append(v4 - 1)
        v6, v7 = (bfs(v2, 0), bfs(v2, a1 - 1))
        v8 = v6[a1 - 1] + 2
        for v9 in range(a1):
            if v6[v9] + v7[v9] == v6[a1 - 1]:
                continue
            v8 = min(v8, v6[v9] + v7[v9])
            if v8 == v6[a1 - 1] + 1:
                break
        return calc_time(a3, a4, v8)
