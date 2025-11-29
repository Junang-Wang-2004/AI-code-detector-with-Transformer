import collections

class C1(object):

    def longestSpecialPath(self, a1, a2):
        """
        """

        def iter_dfs():
            v1 = [float('inf')] * 2
            v2 = collections.defaultdict(lambda: -1)
            v3 = [0]
            v4 = [(1, (0, -1, 0, -1))]
            while v4:
                v5, v6 = v4.pop()
                if v5 == 1:
                    v7, v8, v9, v10 = v6
                    v11, v2[a2[v7] - 1] = (v2[a2[v7] - 1], v9)
                    v10 = max(v10, v11)
                    v1 = min(v1, [-(v3[v9 - 1 + 1] - v3[v10 + 1]), v9 - v10])
                    v4.append((4, (v7, v11)))
                    v4.append((2, (v7, v8, v9, v10, 0)))
                elif v5 == 2:
                    v7, v8, v9, v10, v12 = v6
                    if v12 == len(adj[v7]):
                        continue
                    v4.append((2, (v7, v8, v9, v10, v12 + 1)))
                    v13, v14 = adj[v7][v12]
                    if v13 == v8:
                        continue
                    v3.append(v3[-1] + v14)
                    v4.append((3, None))
                    v4.append((1, (v13, v7, v9 + 1, v10)))
                elif v5 == 3:
                    v3.pop()
                elif v5 == 4:
                    v7, v11 = v6
                    v2[a2[v7] - 1] = v11
            return [-v1[0], v1[1]]
        v1 = [[] for v2 in range(len(a2))]
        for v3, v4, v5 in a1:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        return iter_dfs()
