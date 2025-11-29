class C1(object):

    def longestPath(self, a1, a2):
        """
        """

        def iter_dfs(a1, a2):
            v1 = 0
            v2 = [(1, (0, [0]))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6 = v4
                    v7 = [0] * 2
                    v2.append((4, (v7, v6)))
                    v2.append((2, (v5, 0, v7, v6)))
                elif v3 == 2:
                    v5, v8, v7, v6 = v4
                    if v8 == len(a2[v5]):
                        continue
                    v9 = [0]
                    v2.append((3, (v5, v8, v7, v9)))
                    v2.append((1, (a2[v5][v8], v9)))
                elif v3 == 3:
                    v5, v8, v7, v9 = v4
                    if a1[a2[v5][v8]] != a1[v5]:
                        if v9[0] > v7[0]:
                            v7[0], v7[1] = (v9[0], v7[0])
                        elif v9[0] > v7[1]:
                            v7[1] = v9[0]
                    v2.append((2, (v5, v8 + 1, v7, v6)))
                elif v3 == 4:
                    v7, v6 = v4
                    v1 = max(v1, v7[0] + v7[1] + 1)
                    v6[0] = v7[0] + 1
            return v1
        v1 = [[] for v2 in range(len(a2))]
        for v3 in range(1, len(a1)):
            v1[a1[v3]].append(v3)
        return iter_dfs(a2, v1)
