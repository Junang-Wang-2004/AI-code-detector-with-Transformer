class C1(object):

    def minimumTotalPrice(self, a1, a2, a3, a4):
        """
        """

        def iter_dfs(a1, a2):
            v1 = [(1, (a1, -1))]
            while v1:
                v2, v3 = v1.pop()
                if v2 == 1:
                    a1, v5 = v3
                    lookup[a1] += 1
                    if a1 == a2:
                        return
                    v1.append((2, (a1,)))
                    for v6 in reversed(adj[a1]):
                        if v6 == v5:
                            continue
                        v1.append((1, (v6, a1)))
                elif v2 == 2:
                    a1 = v3[0]
                    lookup[a1] -= 1
            lookup[a1] += 1
            if a1 == a2:
                return True
            for v6 in adj[a1]:
                if v6 == v5:
                    continue
                if dfs(v6, a1, a2):
                    return True
            lookup[a1] -= 1
            return False

        def iter_dfs2():
            v1 = [a3[0] * lookup[0], a3[0] // 2 * lookup[0]]
            v2 = [(1, (0, -1, v1))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6, v7 = v4
                    for v8 in reversed(adj[v5]):
                        if v8 == v6:
                            continue
                        v9 = [a3[v8] * lookup[v8], a3[v8] // 2 * lookup[v8]]
                        v2.append((2, (v9, v7)))
                        v2.append((1, (v8, v5, v9)))
                elif v3 == 2:
                    v9, v7 = v4
                    v7[0] += min(v9)
                    v7[1] += v9[0]
            return min(v1)
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0] * a1
        for v3, v4 in a4:
            iter_dfs(v3, v4)
        return iter_dfs2()
