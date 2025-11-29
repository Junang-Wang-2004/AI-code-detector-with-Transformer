import collections

class C1(object):

    def goodSubtreeSum(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7

        def get_mask(a1):
            v1 = 0
            while a1:
                a1, v3 = divmod(a1, 10)
                if v1 & 1 << v3:
                    return -1
                v1 |= 1 << v3
            return v1

        def iter_dfs():
            v1 = 0
            v2 = collections.defaultdict(int)
            v3 = [(1, (0, v2))]
            while v3:
                v4, v5 = v3.pop()
                if v4 == 1:
                    v6, v2 = v5
                    v2[0] = 0
                    v7 = get_mask(a1[v6])
                    if v7 != -1:
                        v2[v7] = a1[v6]
                    v3.append((4, (v6, v2)))
                    v3.append((2, (v6, 0, v2)))
                elif v4 == 2:
                    v6, v8, v2 = v5
                    if v8 == len(adj[v6]):
                        continue
                    v9 = adj[v6][v8]
                    v3.append((2, (v6, v8 + 1, v2)))
                    v10 = collections.defaultdict(int)
                    v3.append((3, (v10, v2)))
                    v3.append((1, (v9, v10)))
                elif v4 == 3:
                    v10, v2 = v5
                    for v11, v12 in list(v2.items()):
                        for v13, v14 in v10.items():
                            if v11 & v13:
                                continue
                            v2[v11 | v13] = max(v2[v11 | v13], v12 + v14)
                elif v4 == 4:
                    v6, v2 = v5
                    v1 = (v1 + max(v2.values())) % v1
            return v1
        v2 = [[] for v3 in range(len(a1))]
        for v4 in range(1, len(a2)):
            v2[a2[v4]].append(v4)
        return iter_dfs()
