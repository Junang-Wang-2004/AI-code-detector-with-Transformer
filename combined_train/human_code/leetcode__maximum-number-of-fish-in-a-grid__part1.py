class C1(object):

    def findMaxFish(self, a1):
        """
        """
        v1 = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def bfs(a1, a2):
            v1 = a1[a1][a2]
            a1[a1][a2] = 0
            v2 = [(a1, a2)]
            while v2:
                v3 = []
                for a1, a2 in v2:
                    for v6, v7 in v1:
                        v8, v9 = (a1 + v6, a2 + v7)
                        if not (0 <= v8 < len(a1) and 0 <= v9 < len(a1[0]) and a1[v8][v9]):
                            continue
                        v1 += a1[v8][v9]
                        a1[v8][v9] = 0
                        v3.append((v8, v9))
                v2 = v3
            return v1
        v2 = 0
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                if a1[v3][v4]:
                    v2 = max(v2, bfs(v3, v4))
        return v2
