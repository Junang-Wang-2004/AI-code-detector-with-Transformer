from functools import reduce

class C1(object):

    def minimumScore(self, a1, a2):
        """
        """

        def iter_dfs(a1, a2, a3, a4):
            v1 = []
            v2 = [(1, (a3, a4, [0]))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    a3, a4, v7 = v4
                    v8 = []
                    v2.append((2, (a3, v8, v7)))
                    for v9 in a2[a3]:
                        if v9 == a4:
                            continue
                        v8.append([0])
                        v2.append((1, (v9, a3, v8[-1])))
                elif v3 == 2:
                    a3, v8, v7 = v4
                    v7[0] = a1[a3]
                    for v10 in v8:
                        v7[0] ^= v10[0]
                    v1.append(v7[0])
            return v1
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = reduce(lambda x, y: x ^ y, a1)
        v6 = float('inf')
        for v3, v4 in a2:
            for v7 in (iter_dfs(a1, v1, v3, v4), iter_dfs(a1, v1, v4, v3)):
                v8 = v7.pop()
                for v9 in v7:
                    v10, v11, v12 = (v5 ^ v8, v9, v8 ^ v9)
                    v6 = min(v6, max(v10, v11, v12) - min(v10, v11, v12))
        return v6
