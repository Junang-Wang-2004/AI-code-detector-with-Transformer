class C1(object):

    def sumRemoteness(self, a1):
        """
        """
        v1 = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def bfs(a1, a2):
            v1, v2 = (a1[a1][a2], 1)
            a1[a1][a2] = -1
            v3 = [(a1, a2)]
            while v3:
                v4 = []
                for a1, a2 in v3:
                    for v7, v8 in v1:
                        v9, v10 = (a1 + v7, a2 + v8)
                        if not (0 <= v9 < len(a1) and 0 <= v10 < len(a1[0]) and (a1[v9][v10] != -1)):
                            continue
                        v1 += a1[v9][v10]
                        v2 += 1
                        a1[v9][v10] = -1
                        v4.append((v9, v10))
                v3 = v4
            return (v1, v2)
        v2 = [bfs(i, j) for v3 in range(len(a1)) for v4 in range(len(a1[0])) if a1[v3][v4] != -1]
        v5 = sum((t for v6, v7 in v2))
        return sum(((v5 - v6) * c for v6, v8 in v2))
