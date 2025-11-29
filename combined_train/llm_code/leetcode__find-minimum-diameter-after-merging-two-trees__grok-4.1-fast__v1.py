class C1(object):

    def minimumDiameterAfterMerge(self, a1, a2):

        def compute_diameter(a1):
            v1 = len(a1) + 1
            v2 = [[] for v3 in range(v1)]
            for v4, v5 in a1:
                v2[v4].append(v5)
                v2[v5].append(v4)

            def level_bfs(a1):
                v1 = [False] * v1
                v1[a1] = True
                v2 = [a1]
                v3 = a1
                v4 = 0
                while v2:
                    v5 = []
                    for v6 in v2:
                        for v7 in v2[v6]:
                            if not v1[v7]:
                                v1[v7] = True
                                v5.append(v7)
                    if v5:
                        v3 = v5[-1]
                        v2 = v5
                        v4 += 1
                    else:
                        break
                return (v3, v4)
            v6, v3 = level_bfs(0)
            v3, v7 = level_bfs(v6)
            return v7
        v1 = compute_diameter(a1)
        v2 = compute_diameter(a2)
        v3 = (v1 + 1) // 2
        v4 = (v2 + 1) // 2
        return max(v3 + v4 + 1, v1, v2)
