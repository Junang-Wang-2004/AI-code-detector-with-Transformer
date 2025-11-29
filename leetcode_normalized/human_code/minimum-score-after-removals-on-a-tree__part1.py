from functools import reduce

class C1(object):

    def minimumScore(self, a1, a2):
        """
        """

        def is_ancestor(a1, a2):
            return left[a1] <= left[a2] and right[a2] <= right[a1]

        def iter_dfs():
            v1 = 0
            v2 = [0] * len(a1)
            v3 = [0] * len(a1)
            v4 = [(1, (0, -1))]
            while v4:
                v5, v6 = v4.pop()
                if v5 == 1:
                    v7, v8 = v6
                    v2[v7] = v1
                    v1 += 1
                    v4.append((2, (v7, v8)))
                    for v9 in adj[v7]:
                        if v9 == v8:
                            continue
                        v4.append((1, (v9, v7)))
                elif v5 == 2:
                    v7, v8 = v6
                    for v9 in adj[v7]:
                        if v9 == v8:
                            continue
                        a1[v7] ^= a1[v9]
                    v3[v7] = v1
            return (v2, v3)
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5, v6 = iter_dfs()
        v7 = float('inf')
        for v8 in range(1, len(a1)):
            for v9 in range(v8 + 1, len(a1)):
                if is_ancestor(v8, v9):
                    v10, v11, v12 = (a1[0] ^ a1[v8], a1[v8] ^ a1[v9], a1[v9])
                elif is_ancestor(v9, v8):
                    v10, v11, v12 = (a1[0] ^ a1[v9], a1[v9] ^ a1[v8], a1[v8])
                else:
                    v10, v11, v12 = (a1[0] ^ a1[v8] ^ a1[v9], a1[v8], a1[v9])
                v7 = min(v7, max(v10, v11, v12) - min(v10, v11, v12))
        return v7
