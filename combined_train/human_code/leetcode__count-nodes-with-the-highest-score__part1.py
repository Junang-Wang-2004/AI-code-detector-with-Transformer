from functools import reduce

class C1(object):

    def countHighestScoreNodes(self, a1):
        """
        """

        def iter_dfs(a1):
            v1 = [0] * 2
            v2 = [(1, (0, [0]))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6 = v4
                    v7 = [[0] for v8 in range(len(a1[v5]))]
                    v2.append((2, (v7, v6)))
                    for v9, v10 in enumerate(a1[v5]):
                        v2.append((1, (v10, v7[v9])))
                elif v3 == 2:
                    v7, v6 = v4
                    v6[0] = sum((cnt[0] for v11 in v7)) + 1
                    v12 = max(len(a1) - v6[0], 1) * reduce(lambda x, y: x * y[0], v7, 1)
                    if v12 > v1[0]:
                        v1[:] = [v12, 1]
                    elif v12 == v1[0]:
                        v1[1] += 1
            return v1[1]
        v1 = [[] for v2 in range(len(a1))]
        for v3 in range(1, len(a1)):
            v1[a1[v3]].append(v3)
        return iter_dfs(v1)
