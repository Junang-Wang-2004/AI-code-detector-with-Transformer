class C1(object):

    def countIslands(self, a1, a2):
        """
        """
        v1 = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def bfs(a1, a2):
            if not a1[a1][a2]:
                return False
            v1 = a1[a1][a2] % a2
            a1[a1][a2] = 0
            v2 = [(a1, a2)]
            while v2:
                v3 = []
                for a1, a2 in v2:
                    for v6, v7 in v1:
                        v8, v9 = (a1 + v6, a2 + v7)
                        if not (0 <= v8 < len(a1) and 0 <= v9 < len(a1[0]) and a1[v8][v9]):
                            continue
                        v1 = (v1 + a1[v8][v9]) % a2
                        a1[v8][v9] = 0
                        v3.append((v8, v9))
                v2 = v3
            return v1 == 0
        return sum((bfs(i, j) for v2 in range(len(a1)) for v3 in range(len(a1[0]))))
